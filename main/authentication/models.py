from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):

    ROLES = [
        (1, 'Manager'),
        (2, 'User'),
    ]
    email = models.EmailField()

    role = models.PositiveSmallIntegerField(("role"), choices=ROLES, default=2)
