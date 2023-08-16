from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True)
    phone_number = PhoneNumberField(unique = True, null = True, blank = False)
    major = models.CharField(max_length=32, blank=True)
    grade = models.IntegerField(default=0)  
    position = models.CharField(max_length=32, blank=True)
    pitcher = models.BooleanField(default=0)



    
    def __str__(self):
        return f"id={self.id}, user_id={self.user.id},  major={self.major}, position={self.position}"