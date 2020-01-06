from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import models
from books import models as books_models
from . import serializers

class LoanBookViewset(viewsets.ModelViewSet):
    serializer_class = serializers.LoanBookSerializer

    def get_queryset(self):
        queryset = models.LoanBook.objects.filter(book__owner = self.request.user)
        return queryset
