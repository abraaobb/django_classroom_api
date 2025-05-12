from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Person(BaseModel):
    class PersonType(models.TextChoices):
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=7, choices=PersonType.choices)

    def __str__(self):
        return self.name
