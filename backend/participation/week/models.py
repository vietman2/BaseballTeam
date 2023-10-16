from django.db import models

class Week(models.Model):
    month_week  = models.CharField(max_length=10, blank=False, null=False, db_comment="월-주차")
    start_date  = models.DateField(blank=False, null=False, db_comment="시작일 (월)")
    end_date    = models.DateField(blank=False, null=False, db_comment="종료일 (일)")

    monday      = models.ForeignKey(
        "Session",
        on_delete=models.DO_NOTHING,
        related_name='monday',
        blank=True,
        null=True
    )
    tuesday     = models.ForeignKey(
        "Session",
        on_delete=models.DO_NOTHING,
        related_name='tuesday',
        blank=True,
        null=True
    )
    wednesday   = models.ForeignKey(
        "Session",
        on_delete=models.DO_NOTHING,
        related_name='wednesday',
        blank=True,
        null=True
    )
    thursday    = models.ForeignKey(
        "Session",
        on_delete=models.DO_NOTHING,
        related_name='thursday',
        blank=True,
        null=True
    )
    friday      = models.ForeignKey(
        "Session",
        on_delete=models.DO_NOTHING,
        related_name='friday',
        blank=True,
        null=True
    )
    saturday    = models.ForeignKey(
        "Session",
        on_delete=models.DO_NOTHING,
        related_name='saturday',
        blank=True,
        null=True
    )
    sunday      = models.ForeignKey(
        "Session",
        on_delete=models.DO_NOTHING,
        related_name='sunday',
        blank=True,
        null=True
    )

    class Meta:
        db_table            = 'week'
        verbose_name        = 'week'
        verbose_name_plural = 'weeks'
        db_table_comment    = "훈련"
