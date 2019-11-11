from django.urls import path
from .views import LoanBookView, ReturnBookView, BookNotAvailable

app_name = 'rental'

urlpatterns = [
    path('loan-book/<int:pk>/', LoanBookView.as_view(), name='loan-book'),
    path('return-book/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
    path('book-not-available/<int:pk>/', BookNotAvailable.as_view(), name='book-not-available'),
    ]
