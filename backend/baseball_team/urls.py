from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView as SSV,
    SpectacularRedocView as SRV,
)

from user.views import UserViewSet, MyLoginView as LoginView, MyLogoutView as LogoutView
from participation.session.views import TrainingTypeViewSet
from participation.week.views import WeekViewSet

router = DefaultRouter()

router.register(prefix=r'users', viewset=UserViewSet, basename='user')
router.register(prefix=r'trainingtypes', viewset=TrainingTypeViewSet, basename='trainingtype')
router.register(prefix=r'weeks', viewset=WeekViewSet, basename='week')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SSV.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SRV.as_view(url_name='schema'), name='redoc'),
]
