from rest_framework import viewsets

from books.permissions import IsOwner
from . import models
from . import serializers

class BooksViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        queryset = models.Books.objects.filter(owner = self.request.user)
        return queryset

