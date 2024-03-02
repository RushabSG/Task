from django.db import models

# Create your models here.


class ShortUrlModel(models.Model):

    original_url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.original_url
