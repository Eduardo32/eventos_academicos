from turtledemo import yinyang

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from datetime import datetime

from locations.models import Estado, Cidade


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        null=True,
    )

    cidade = models.ForeignKey(
        Cidade,
        on_delete=models.SET_NULL,
        null=True,
    )

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
