from django.db import models
from books.models import Books

# Create your models here.
class LoanBook(models.Model):
    book = models.OneToOneField(Books, on_delete=models.CASCADE)
    date = models.DateField()
    friend_name = models.CharField(max_length=50)
    friend_surname = models.CharField(max_length=50)
    friend_email = models.EmailField()

    def __str__(self):
        return f'{self.book.title} - {self.friend_email} ({self.date})'

    class Meta:
        verbose_name_plural = "Wypożyczenia książek"
        verbose_name = "Wypożyczone książki"