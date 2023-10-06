from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from .managers import ActiveMembersManager, UserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
    class UserType(models.IntegerChoices):
        NEW_ACCOUNT = 0, '신규계정'
        ADMIN = 1, '관리자'
        CAPTAIN = 2, '주장'
        VICE_CAPTAIN = 3, '부주장'
        MANAGER = 4, '매니저'
        MEMBER = 5, '부원'
        MILITARY = 6, '군입대자'
        INACTIVE = 7, '비활동부원'
        DELETED = 8, '탈퇴한 회원'

    class Positions(models.IntegerChoices):
        NEW = 0, '신입'
        PITCHER = 1, '투수'
        CATCHER = 2, '포수'
        FIRST_BASEMAN = 3, '1루수'
        SECOND_BASEMAN = 4, '2루수'
        THIRD_BASEMAN = 5, '3루수'
        SHORTSTOP = 6, '유격수'
        LEFT_FIELDER = 7, '좌익수'
        CENTER_FIELDER = 8, '중견수'
        RIGHT_FIELDER = 9, '우익수'

    ## 기본 정보
    user_type = models.IntegerField(choices=UserType.choices, default=UserType.NEW_ACCOUNT)
    name = models.CharField(max_length=32, db_comment="이름")
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[RegexValidator(r'^010-\d{4}-\d{4}$')],
        db_comment="전화번호는 '010-xxxx-xxxx' 형식으로만 받음",
        error_messages={
            'invalid': "전화번호는 '010-xxxx-xxxx' 형식으로만 받습니다",
            'unique': '이미 존재하는 전화번호입니다'
        }
    )
    date_joined = models.DateTimeField(auto_now_add=True, db_comment="가입일")
    last_login = models.DateTimeField(auto_now=True, db_comment="마지막 로그인 시간")
    is_active = models.BooleanField(default=True, db_comment="로그인 가능 여부")
    # 비밀번호는 AbstractBaseUser에 있음

    ## 추가 정보
    major = models.CharField(
        max_length=32,
        db_comment="학부/학과명. 개발의 편의를 위해 CharField로 받고, 형식은 자유. 단, 비어있으면 안됨",
        default="전공없음",
    )
    grade = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        error_messages={'invalid': "학년은 1~4만 가능합니다"}
    )
    position = models.IntegerField(choices=Positions.choices, default=Positions.NEW)

    objects = UserManager()
    active_members = ActiveMembersManager() ## 활동중인 부원에 대한 정보를 반환하는 매니저

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table_comment = "야구부 부원들의 정보를 담는 테이블"
