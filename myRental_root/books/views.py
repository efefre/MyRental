from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from .models import Books


# Create your views here.
@method_decorator(login_required, name='dispatch')
class BooksList(View):
    template_name = 'rental/books.html'
    model = Books

    def get(self, request, *args, **kwargs):
        user_books = self.model.objects.filter(owner = request.user)
        context = {
            'user_books' : user_books
        }
        return render(request, self.template_name, context)
