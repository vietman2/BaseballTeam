from django.apps import apps
from rest_framework.permissions import BasePermission

USERTYPE = apps.get_model('account', 'CustomUser').UserType

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == USERTYPE.ADMIN
    
class IsCaptain(BasePermission):
    def has_permission(self, request, view):
        # 주장
        return request.user.user_type == USERTYPE.CAPTAIN
    
class IsLeadership(BasePermission):
    def has_permission(self, request, view):
        ## 주장, 부주장, 매니저
        return request.user.user_type in [
            USERTYPE.CAPTAIN,
            USERTYPE.VICE_CAPTAIN,
            USERTYPE.MANAGER
        ]
    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        # 매니저
        return request.user.user_type == USERTYPE.MANAGER
    
class IsActiveMember(BasePermission):
    def has_permission(self, request, view):
        # 주장, 부주장, 매니저, 부원
        return request.user.user_type in [
            USERTYPE.CAPTAIN,
            USERTYPE.VICE_CAPTAIN,
            USERTYPE.MANAGER,
            USERTYPE.MEMBER
        ]
