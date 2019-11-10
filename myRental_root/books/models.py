from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Books(models.Model):
    AVAILABLE = 'AV'
    LOAN = 'LO'

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (LOAN, 'On loan')
    )

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'Book: {self.title}, Author: {self.author}'

    class Meta:
        unique_together = ('title', 'author', 'owner',)
        verbose_name_plural = "Książki"
        verbose_name = "Książka"
