from django.urls import path
from .views import BooksList

app_name = 'books'

urlpatterns = [
    path('', BooksList.as_view(), name='books-list'),
    ]
