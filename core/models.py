from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    class Optional(models.TextChoices):
        DBMS='DB','DBMS'
        NETWORKING='NET','networking'

    name = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    optional=models.CharField(max_length=50,choices=Optional.choices)

    def __str__(self):
        return self.name
    