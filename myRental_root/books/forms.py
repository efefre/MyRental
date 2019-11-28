from django import forms
from django.core.exceptions import ValidationError

from books.models import Books


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Books
        exclude = ['owner', 'status']

    def clean(self):
        cleaned_data = self.cleaned_data
        if Books.objects.filter(title=cleaned_data['title'],
                                author=cleaned_data['author'],
                                owner = self.request.user).exists():
            raise ValidationError('Książka już istnieje')

        return cleaned_data


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
