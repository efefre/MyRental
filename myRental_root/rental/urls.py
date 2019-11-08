from django.urls import path
from .views import BooksList


urlpatterns = [
    path('', BooksList.as_view(), name='books-list'),
    ]