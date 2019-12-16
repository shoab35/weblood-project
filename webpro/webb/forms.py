from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserFormUpdate(forms.ModelForm):
    class Meta():
        model = User
        fields = ['email']


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', 'First_name', 'Last_name', 'age', 'weight', 'blood_group', 'District', 'phone_number',
                  'status')


class UserProfileInfoFormUpdate(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', 'First_name', 'Last_name', 'age', 'weight', 'District', 'phone_number', 'status')
