from django import forms
from books.models import Books


class AddBookForm(forms.ModelForm):

    class Meta:
        model = Books
        exclude = ['owner', 'status']
