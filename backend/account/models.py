from django.db import models
from django.contrib.auth.models import User, AbstractUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(AbstractUser,PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "관리자","관리자"
        LEADER = "주장단","주장단"
        MANAGER = "매니저","매니저"
        PLAYER = "부원","부원"
    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices,default=base_role)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True)
    phone_number = PhoneNumberField(unique = True, null = True, blank = False)
    major = models.CharField(max_length=32, blank=True)
    grade = models.IntegerField(default=0)
    position = models.CharField(max_length=32, blank=True)
    pitcher = models.BooleanField(default=False)




    
    def __str__(self):
        return f"user_id={self.user.username}"