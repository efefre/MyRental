from django.views.generic import FormView
from .forms import LoanBookForm
from books.models import Books

# Create your views here.
class LoanBookView(FormView):
    template_name = 'rental/loan_book.html'
    form_class = LoanBookForm
    success_url = '/books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Books.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        context = self.get_context_data()
        form.book = context['book']
        form.save()
        return super().form_valid(form)
