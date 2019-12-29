from rest_framework import routers
from books import api_views as books_views
from rental import api_views as rental_views

router = routers.DefaultRouter()
router.register(r'books', books_views.BooksViewset, basename='Books')
router.register(r'loan-book', rental_views.LoanBookViewset, basename='LoanBook')
