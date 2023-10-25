from django.contrib import admin

from .models import Session, TrainingType, Attendance

admin.site.register(Session)
admin.site.register(TrainingType)
admin.site.register(Attendance)
