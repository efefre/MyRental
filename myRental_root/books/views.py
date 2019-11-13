from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View
from django.views.generic.base import ContextMixin

from .models import Books
from rental.models import LoanBook
from .forms import AddBookForm


# Create your views here.
class LoanDetailContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loan_book = LoanBook.objects.all()
        context = loan_book
        return context


@method_decorator(login_required, name='dispatch')
class BooksList(LoanDetailContextMixin, View):
    template_name = 'books/books.html'
    model = Books

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx

    def get(self, request, *args, **kwargs):
        user_books = self.model.objects.filter(owner = request.user).order_by('-status', 'title')
        page = request.GET.get('page', 1)

        paginator = Paginator(user_books, 10)

        try:
            user_books = paginator.page(page)
        except PageNotAnInteger:
            user_books = paginator.page(1)
        except EmptyPage:
            user_books = paginator.page(paginator.num_pages)

        context = {
            'user_books' : user_books,
            'loan_detail' : self.get_context_data(),
        }
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class AddBookView(FormView):
    template_name = 'books/add_book.html'
    form_class = AddBookForm
    success_url = '/books'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.owner = self.request.user
        form.save()
        return super().form_valid(form)