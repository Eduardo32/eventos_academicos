from turtledemo import yinyang

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from datetime import datetime, timedelta


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    university = models.CharField(
        max_length=30
    )

    birth = models.DateField()

    def age(self):
        now = datetime.now()
        age = now.date().year - self.birth.year

        if (self.birth.month > now.date().month) \
                or ((self.birth.month == now.date().month) and (self.birth.day > now.date().day)):
            age -= 1

        return age

    objects = CustomUserManager()
