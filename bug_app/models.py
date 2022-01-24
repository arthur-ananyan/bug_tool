from django.db import models
from django.contrib.auth.models import User


class Bug(models.Model):

    class Status(models.IntegerChoices):
        UNRESOLVED = 0
        RESOLVED = 1

    title = models.CharField(max_length=150)
    body = models.TextField(max_length=1000)
    status = models.IntegerField(choices=Status.choices, default=Status.UNRESOLVED)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=1000)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


