from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm, UserFormUpdate, UserProfileInfoFormUpdate
from .models import UserProfileInfo
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'webb/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def user_profile(request):
    return render(request, 'webb/userprofile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_update_form = UserFormUpdate(request.POST, instance=request.user)
        profile_update_form = UserProfileInfoFormUpdate(request.POST,
                                                        request.FILES,
                                                        instance=request.user.userprofileinfo)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            return redirect('edit_profile')
    else:
        user_update_form = UserFormUpdate(instance=request.user)
        profile_update_form = UserProfileInfoFormUpdate(instance=request.user.userprofileinfo)

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'webb/editprofile.html', context)


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'webb/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password {}".format(username, password))
            return HttpResponse("invalid details supplied")

    else:
        return render(request, 'webb/login.html', {})


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = UserProfileInfo.objects.filter(Q(blood_group__icontains=srch) |
                                                   Q(District__icontains=srch) |
                                                   Q(First_name__icontains=srch) |
                                                   Q(Last_name__icontains=srch)
                                                   )
            if match:
                return render(request, 'webb/search.html', {'sr': match})
            else:
                return redirect('search')
        else:
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'webb/base.html')
