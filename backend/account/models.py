from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin

관리자 = 1
주장단 = 2
부원 = 3

ROLE_CHOICES = (
    (관리자, '관리자'),
    (주장단, '주장단'),
    (부원, '부원'),
)

class CustomUser(AbstractUser,PermissionsMixin):
    name = models.CharField(max_length=32, blank=True)
    major = models.CharField(max_length=32, blank=True)
    grade = models.IntegerField(default=0, blank=True)
    position = models.CharField(max_length=32, blank=True)
    is_pitcher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    
