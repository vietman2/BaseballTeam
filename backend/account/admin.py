from django.contrib import admin

# Register your models here.
from .models import CustomUser,UserProfile   # 추가

admin.site.register(CustomUser)
admin.site.register(UserProfile)  # 추가
