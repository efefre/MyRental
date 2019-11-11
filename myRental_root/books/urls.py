from django.urls import path
from .views import BooksList, AddBookView

app_name = 'books'

urlpatterns = [
    path('', BooksList.as_view(), name='books-list'),
    path('add-book/', AddBookView.as_view(), name='add-book'),
    ]
