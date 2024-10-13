# models.py in shortener app

from django.db import models
from django.contrib.auth.models import User
import string, random


class ShortURL(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super(ShortURL, self).save(*args, **kwargs)

    def generate_short_url(self):
        length = 6
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choices(characters, k=length))
            if not ShortURL.objects.filter(short_url=short_url).exists():
                return short_url
