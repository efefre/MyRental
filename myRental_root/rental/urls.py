from django.urls import path
from .views import LoanBookView

app_name = 'rental'

urlpatterns = [
    path('loan-book/<int:pk>/', LoanBookView.as_view(), name='loan-book'),
    ]
