from django.db import models

# Create your models here.
class Session(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

class TrainingType(models.Model):
    type = models.CharField(max_length=50)