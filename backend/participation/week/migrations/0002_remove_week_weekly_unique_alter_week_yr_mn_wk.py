# Generated by Django 4.2.4 on 2023-10-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='week',
            name='weekly_unique',
        ),
        migrations.AlterField(
            model_name='week',
            name='yr_mn_wk',
            field=models.CharField(db_comment='년-월-주차', max_length=10, unique=True),
        ),
    ]
