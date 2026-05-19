from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import BaseModel


class User(AbstractUser, BaseModel):

    email = models.EmailField(
        unique=True
    )

    full_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    def __str__(self):
        return self.username