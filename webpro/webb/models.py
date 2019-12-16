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
        ('A+', 'A+'), ('A-',  'A-'), ('B+',  'B+'), ('B-',  'B-'), ('AB+',  'AB+'), ('AB-',  'AB-'), ('O+',  'O+'), ('O-',  'O-')
    ]

    blood_group = models.CharField(max_length=10, choices=bg, blank=False)

    phone_number = models.IntegerField(blank=False)

    bd = [
        ('Syllhet', 'Syllhet'), ('Habiganj', 'Habiganj'), ('Lalmonirhat', 'Lalmonirhat'), ('Rajshahi', 'Rajshahi'), ('Pabna', 'Pabna'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'),
        ('Tangail', 'Tangail')
    ]

    District = models.CharField(max_length=50, choices=bd, blank=False)

    stat = [
        ('Available', 'AVAILABLE'), ('Unavailable', 'UNAVAILABLE')
    ]

    status = models.CharField(max_length=12, choices=stat, blank=False)

    First_name = models.CharField(max_length=15, blank=False)

    Last_name = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.user.username



