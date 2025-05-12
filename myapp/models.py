from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Person(BaseModel):
    class PersonType(models.TextChoices):
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'

    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=False, unique=True)
    type = models.CharField(max_length=7, choices=PersonType.choices)

    def __str__(self):
        return self.name


class Classroom(BaseModel):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='classrooms')


class Enrollment(BaseModel):
    student = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='enrollments')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='enrollments')

    class Meta:
        unique_together = ['student', 'classroom']
