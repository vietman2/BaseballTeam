from django.db import models
from tag.models import Tag

# Create your models here.
class Forecast(models.Model) :
    temperature = models.IntegerField
    description = models.CharField

class Timetable(models.Model) :
    date = models.DateField
    forecast = models.ForeignKey(Forecast, on_delete=models.CASCADE)
    total = models.IntegerField
    drilltype = models.CharField
    tags = models.ManyToManyField(Tag, blank=True, related_name='timetables')

    