from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView, DeleteView, TemplateView
from .forms import LoanBookForm
from books.models import Books
from .models import LoanBook


# Create your views here.
@method_decorator(login_required, name='dispatch')
class BookNotAvailable(TemplateView):
    template_name = 'rental/book_not_available.html'


@method_decorator(login_required, name='dispatch')
class LoanBookView(FormView):
    template_name = 'rental/loan_book.html'
    form_class = LoanBookForm
    success_url = '/books'

    def dispatch(self, request, *args, **kwargs):
        if LoanBook.objects.filter(book_id=self.kwargs.get('pk')).exists():
            return redirect(reverse('rental:book-not-available', kwargs={'pk':self.kwargs.get('pk')}))
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Books.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        context = self.get_context_data()
        form.book = context['book']
        context['book'].save()
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ReturnBookView(DeleteView):
    model = LoanBook
    template_name = 'rental/confirm_return.html'
    context_object_name = 'return'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        loan_book_object = LoanBook.objects.get(book_id = pk)
        return loan_book_object

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        book = Books.objects.get(pk=self.kwargs.get('pk'))
        book.status = 'AV'
        book.save()
        return redirect(reverse('books:books-list'))
