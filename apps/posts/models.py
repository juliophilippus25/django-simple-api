from django.db import models

from apps.core.models import BaseModel
from apps.authentication.models import User


class Post(BaseModel):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    is_published = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title