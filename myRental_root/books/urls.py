from django.urls import path
from .views import BooksList, AddBookView, UpdateBookView

app_name = 'books'

urlpatterns = [
    path('', BooksList.as_view(), name='books-list'),
    path('add-book/', AddBookView.as_view(), name='add-book'),
    path('update-book/<int:pk>', UpdateBookView.as_view(), name='update-book'),
    ]
