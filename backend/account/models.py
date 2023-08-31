from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser,PermissionsMixin):
    관리자 = 1
    주장단 = 2
    부원 = 3

    ROLE_CHOICES = (
        (관리자, '관리자'),
        (주장단, '주장단'),
        (부원, '부원'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    phone_number = PhoneNumberField(unique=True, null=True, blank=False)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True)
    major = models.CharField(max_length=32, blank=True)
    grade = models.IntegerField(default=0)
    position = models.CharField(max_length=32, blank=True)
    pitcher = models.BooleanField(default=False)
