from django.contrib import admin

# Register your models here.
from .models import CustomUser   # 추가

admin.site.register(CustomUser)
