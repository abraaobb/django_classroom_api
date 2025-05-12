from rest_framework import viewsets

from myapp import models, serializers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = models.Classroom.objects.all()
    serializer_class = serializers.ClassroomSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
