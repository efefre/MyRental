from django import forms
from rental.models import LoanBook


class LoanBookForm(forms.ModelForm):

    class Meta:
        model = LoanBook
        fields = ('date', 'friend_name', 'friend_surname', 'friend_email')

        widgets = {'date': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'type':'date'}),
                   'friend_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'friend_surname': forms.TextInput(attrs={'class': 'form-control'}),
                   'friend_email': forms.EmailInput(attrs={'class': 'form-control'})
                   }
