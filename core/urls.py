from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from myapp import viewsets

router = routers.DefaultRouter()
router.register('people', viewsets.PersonViewSet)
router.register('classrooms', viewsets.ClassroomViewSet)
router.register('enrollments', viewsets.EnrollmentViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
