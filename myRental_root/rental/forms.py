from django import forms
from rental.models import LoanBook


class LoanBookForm(forms.ModelForm):

    class Meta:
        model = LoanBook
        fields = ('date', 'friend_name', 'friend_surname', 'friend_email')
