from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    phone_no = models.CharField(max_length=10)


