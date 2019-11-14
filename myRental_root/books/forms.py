from django import forms
from books.models import Books


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Books
        exclude = ['owner', 'status']
