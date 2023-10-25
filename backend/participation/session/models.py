from django.db import models

class Session(models.Model):
    class DayChoices(models.IntegerChoices):
        MON = 1, "월요일"
        TUE = 2, "화요일"
        WED = 3, "수요일"
        THU = 4, "목요일"
        FRI = 5, "금요일"
        SAT = 6, "토요일"
        SUN = 7, "일요일"

    date = models.DateField(db_comment="훈련 날짜")
    day = models.IntegerField(choices=DayChoices.choices, db_comment="훈련 요일")
    start_time = models.TimeField(db_comment="훈련 시작 시간")
    end_time = models.TimeField(db_comment="훈련 종료 시간")
    training_type = models.ForeignKey("TrainingType", on_delete=models.DO_NOTHING, related_name='sessions')

    class Meta:
        ordering = ['date', 'start_time']
        db_table = 'session'
        verbose_name = 'session'
        verbose_name_plural = 'sessions'
        db_table_comment = "세션 = 훈련 한 타임"

class TrainingType(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'training_type'
        verbose_name = 'training_type'
        verbose_name_plural = 'training_types'
        db_table_comment = "훈련 유형"

class Attendance(models.Model):
    user = models.ForeignKey("account.CustomUser", on_delete=models.CASCADE)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    is_coming = models.BooleanField(default=False)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'attendance'
        verbose_name = 'attendance'
        verbose_name_plural = 'attendances'
        db_table_comment = "출석"
        unique_together = ['user', 'session']
