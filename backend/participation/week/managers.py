import datetime
from django.db import models

from participation.session.models import Session, TrainingType

class WeekManager(models.Manager):
    def is_week_created(self, yr_mn_wk):
        return self.filter(yr_mn_wk=yr_mn_wk).exists()
    
    def create_session(self, day, data):
        def get_day(day):
            if day == "monday":
                return Session.DayChoices.MON
            elif day == "tuesday":
                return Session.DayChoices.TUE
            elif day == "wednesday":
                return Session.DayChoices.WED
            elif day == "thursday":
                return Session.DayChoices.THU
            elif day == "friday":
                return Session.DayChoices.FRI
            elif day == "saturday":
                return Session.DayChoices.SAT
            elif day == "sunday":
                return Session.DayChoices.SUN
            else:
                raise ValueError("Invalid day")

        training_type = TrainingType.objects.get(pk=data[day]["training_type"]["id"])

        if training_type.type == "훈련없음":
            day = Session.objects.create(
                date=data[day]["date"],
                day=get_day(day),
                training_type=training_type,
            )
            return day
        else:
            start_time = datetime.time(
                data[day]["start_time"]["hour"],
                data[day]["start_time"]["minute"]
            )
            end_time = datetime.time(
                data[day]["end_time"]["hour"],
                data[day]["end_time"]["minute"]
            )
            day = Session.objects.create(
                date=data[day]["date"],
                day=get_day(day),
                start_time=start_time,
                end_time=end_time,
                training_type=training_type,
            )
            return day
