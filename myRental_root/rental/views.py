from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoanBookForm

# Create your views here.
class LoanBookView(FormView):
    template_name = 'rental/loan_book.html'
    form_class = LoanBookForm
    success_url = '/books'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
