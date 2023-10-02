from django.db import models
from account.models import CustomUser
from session.models import Session

# Create your models here.
class Attendance:
  user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
  session = models.ForeignKey("Session", on_delete=models.CASCADE)
  start_time = models.TimeField()
  end_time = models.TimeField()