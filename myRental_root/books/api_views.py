from rest_framework import viewsets

from books.permissions import IsOwner
from . import models
from . import serializers

class BooksViewset(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializer
    permission_classes = [IsOwner]
