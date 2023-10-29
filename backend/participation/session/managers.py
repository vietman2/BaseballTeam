from django.db import models

class SessionManager(models.Manager):
    def create(self, date, day, training_type, **kwargs):
        session = self.model(
            date=date,
            day=day,
            training_type=training_type,
            **kwargs
        )
        session.save()
        return session
