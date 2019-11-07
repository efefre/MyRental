from django.conf import settings
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Profile: {self.user.username}'
