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
    def create_user(self, name, phone_number, password=None, **extra_fields):
        user = self.model(
            name=name,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        CustomUser = apps.get_model('user', 'CustomUser')

        user = self.model(
            name=name,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.user_type = CustomUser.UserType.ADMIN
        user.save(using=self._db)

        return user

    def delete_user(self, user):
        ## 실제로 삭제하지 말고, is_active를 False로 바꾸는 것으로 대체
        CustomUser = apps.get_model('user', 'CustomUser')

        user.is_active = False
        user.user_type = CustomUser.UserType.DELETED
        user.save(using=self._db)

        return user

    def handover_leadership(self, data):
        old_captain = self.get(phone_number=data['old_captain'])
        old_vice_captain = self.get(phone_number=data['old_vice_captain'])
        new_captain = self.get(phone_number=data['new_captain'])
        new_vice_captain = self.get(phone_number=data['new_vice_captain'])

        CustomUser = apps.get_model('user', 'CustomUser')

        old_captain.user_type = CustomUser.UserType.MEMBER
        old_captain.save(using=self._db)

        old_vice_captain.user_type = CustomUser.UserType.MEMBER
        old_vice_captain.save(using=self._db)

        new_captain.user_type = CustomUser.UserType.CAPTAIN
        new_captain.save(using=self._db)

        new_vice_captain.user_type = CustomUser.UserType.VICE_CAPTAIN
        new_vice_captain.save(using=self._db)

        return old_captain, old_vice_captain, new_captain, new_vice_captain

    def change_user_type(self, data):
        user = self.get(phone_number=data['phone_number'])

        CustomUser = apps.get_model('user', 'CustomUser')

        user.user_type = CustomUser.UserType[data['new_status']]
        user.save(using=self._db)

        return user

class ActiveMembersManager(models.Manager):
    def get_queryset(self):
        ## UserType이 2, 3, 4, 5 인 사람들만 반환
        return super().get_queryset().filter(user_type__in=[2, 3, 4, 5])
