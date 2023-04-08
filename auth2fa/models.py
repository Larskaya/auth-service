from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    auth_code = models.CharField(max_length=6)


class Token(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.CharField(max_length=100)
    created_at = models.DateTimeField()
