from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    age = models.IntegerField(blank=False)

    weight = models.IntegerField(blank=False)

    bg = [
        ('a+', 'A+'), ('a-',  'A-'), ('b+',  'B+'), ('b-',  'B-'), ('ab+',  'AB+'), ('ab-',  'AB-'), ('o+',  'O+'), ('o-',  'O-')
    ]

    blood_group = models.CharField(max_length=10, choices=bg, blank=False)

    phone_number = models.IntegerField(blank=False)

    bd = [
        ('syllhet', 'Syllhet'), ('habiganj', 'Habiganj'), ('lalmonirhat', 'Lalmonirhat'), ('rajshahi', 'Rajshahi'), ('pabna', 'Pabna'), ('mymensingh', 'Mymensingh'), ('khulna', 'Khulna'),
        ('tangail', 'Tangail')
    ]

    District = models.CharField(max_length=50, choices=bd, blank=False)

    def __str__(self):
        return self.user.username



