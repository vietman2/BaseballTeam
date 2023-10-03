from django.db import models
from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
        CustomUser 모델의 매니저: 유저 생성, 삭제, 수정을 담당한다.
        유저를 생성할 때는 반드시 CustomUser.objects.create_user()를 사용할 것.
        create()나 save()를 사용하면 비밀번호가 암호화되지 않음.
        관리자를 생성할 때는 CustomUser.objects.create_superuser() 사용
    """
    def create_user(self, user_type, name, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('전화번호는 필수입니다')
        if not name:
            raise ValueError('이름은 필수입니다')

        user = self.model(
            user_type=user_type,
            name=name,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser는 True여야 합니다')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff는 True여야 합니다')

        CustomUser = apps.get_model('account', 'CustomUser')    # circular import 방지

        return self.create_user(
            CustomUser.UserType.ADMIN,
            name,
            phone_number,
            password,
            **extra_fields
        )

class ActiveMembersManager(models.Manager):
    def get_queryset(self):
        ## UserType이 2, 3, 4, 5 인 사람들만 반환
        return super().get_queryset().filter(user_type__in=[2, 3, 4, 5])
    
    ## 추후 여기에 필요한 함수 추가. 예를 들어:
    ## def get_captain(self):
    ## def get_managers(self):
    ## def get_pitchers(self):
    ## def is_pitcher(self, user): 등등
    ## 너무 많아지면 추후에 managers.py로 빼도 됨
