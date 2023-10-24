from django.db import models

class Week(models.Model):
    yr_mn_wk    = models.CharField(max_length=10, blank=False, null=False, db_comment="년-월-주차")
    year        = models.IntegerField(blank=False, null=False, db_comment="년")
    month       = models.IntegerField(blank=False, null=False, db_comment="월")
    week        = models.IntegerField(blank=False, null=False, db_comment="주차")
    start_date  = models.DateField(blank=False, null=False, db_comment="시작일 (월)")
    end_date    = models.DateField(blank=False, null=False, db_comment="종료일 (일)")

    monday      = models.ForeignKey(
        "session.Session",
        on_delete=models.DO_NOTHING,
        related_name='monday',
        blank=True,
        null=True
    )
    tuesday     = models.ForeignKey(
        "session.Session",
        on_delete=models.DO_NOTHING,
        related_name='tuesday',
        blank=True,
        null=True
    )
    wednesday   = models.ForeignKey(
        "session.Session",
        on_delete=models.DO_NOTHING,
        related_name='wednesday',
        blank=True,
        null=True
    )
    thursday    = models.ForeignKey(
        "session.Session",
        on_delete=models.DO_NOTHING,
        related_name='thursday',
        blank=True,
        null=True
    )
    friday      = models.ForeignKey(
        "session.Session",
        on_delete=models.DO_NOTHING,
        related_name='friday',
        blank=True,
        null=True
    )
    saturday    = models.ForeignKey(
        "session.Session",
        on_delete=models.DO_NOTHING,
        related_name='saturday',
        blank=True,
        null=True
    )
    sunday      = models.ForeignKey(
        "session.Session",
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
        indexes             = [
            models.Index(fields=['yr_mn_wk',], name='weekly_index'),
        ]
        constraints         = [
            models.UniqueConstraint(fields=['yr_mn_wk',], name='weekly_unique'),
            models.CheckConstraint(check=models.Q(year__gte=2000), name='year_gte_2000'),
            models.CheckConstraint(check=models.Q(year__lte=9999), name='year_lte_9999'),
            models.CheckConstraint(check=models.Q(month__gte=1), name='month_gte_1'),
            models.CheckConstraint(check=models.Q(month__lte=12), name='month_lte_12'),
            models.CheckConstraint(check=models.Q(week__gte=1), name='week_gte_1'),
            models.CheckConstraint(check=models.Q(week__lte=5), name='week_lte_5'),
        ]
