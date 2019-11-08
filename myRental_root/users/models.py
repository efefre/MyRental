from django.conf import settings
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Profile: {self.user.username}'
