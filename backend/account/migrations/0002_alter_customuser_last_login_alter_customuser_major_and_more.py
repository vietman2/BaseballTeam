# Generated by Django 4.2.4 on 2023-10-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True, db_comment='마지막 로그인 시간'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='major',
            field=models.CharField(db_comment='학부/학과명. 개발의 편의를 위해 CharField로 받고, 형식은 자유. 단, 비어있으면 안됨', default='전공없음', max_length=32),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(0, '신규계정'), (1, '관리자'), (2, '주장'), (3, '부주장'), (4, '매니저'), (5, '부원'), (6, '군입대자'), (7, '비활동부원'), (8, '탈퇴한 회원')], default=0),
        ),
    ]
