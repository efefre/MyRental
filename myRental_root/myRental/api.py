from rest_framework import routers
from books import api_views as books_views

router = routers.DefaultRouter()
router.register(r'books', books_views.BooksViewset)
