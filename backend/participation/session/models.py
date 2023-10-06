from django.db import models

class Session(models.Model):
    class DayChoices(models.IntegerChoices):
        MONDAY = 1, "월요일"
        TUESDAY = 2, "화요일"
        WEDNESDAY = 3, "수요일"
        THURSDAY = 4, "목요일"
        FRIDAY = 5, "금요일"
        SATURDAY = 6, "토요일"
        SUNDAY = 7, "일요일"

    date = models.DateField()
    day = models.IntegerField(choices=DayChoices.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    training_type = models.ForeignKey("TrainingType", on_delete=models.SET_NULL, related_name='sessions')

    class Meta:
        ordering = ['date', 'start_time']
        db_table = 'session'
        verbose_name = 'session'
        verbose_name_plural = 'sessions'
        db_table_comment = "세션 = 훈련 한 타임"

class TrainingType(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
