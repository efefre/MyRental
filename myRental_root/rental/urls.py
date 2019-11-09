from django.urls import path
from .views import LoanBookView


urlpatterns = [
    path('loan-book', LoanBookView.as_view(), name='loan-book'),
    ]
