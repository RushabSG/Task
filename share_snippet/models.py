from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
class TextSnippetModel(models.Model):
    text = models.TextField()
    url = models.URLField(max_length=150)
    secret_key = models.CharField(max_length=150)

    def generate_unique_url(self):
        while True:
            unique_url = get_random_string(length=8)
            if not TextSnippetModel.objects.filter(url=unique_url).exists():
                return unique_url
            
    def save(self, *args, **kwargs):
        if not self.url:
            self.url = self.generate_unique_url()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.url}'