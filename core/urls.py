from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from myapp import viewsets

router = routers.DefaultRouter()
router.register('people', viewsets.PersonViewSet)
router.register('classrooms', viewsets.ClassroomViewSet)
router.register('enrollments', viewsets.EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
