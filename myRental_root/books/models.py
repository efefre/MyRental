from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(verbose_name='Tytuł', max_length=200)
    author = models.CharField(verbose_name='Autor', max_length=200)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'Book: {self.title}, Author: {self.author}'

    class Meta:
        unique_together = ('title', 'author', 'owner',)
        verbose_name_plural = "Książki"
        verbose_name = "Książka"
