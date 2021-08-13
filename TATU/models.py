from django.db import models
from django.db.models import manager
from django.db.models.fields import CharField


class Direction(models.Model):
    title = CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=255)
    nation = models.CharField(max_length=255)

    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name



class Klub(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    established_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Futbolchi(models.Model):
    klub = models.OneToOneField(Klub, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    salary = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.fullname






