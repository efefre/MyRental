from rest_framework import viewsets

from . import models
from . import serializers

class LoanBookViewset(viewsets.ModelViewSet):
    serializer_class = serializers.LoanBookSerializer
    queryset = models.LoanBook.objects.all()

    def get_queryset(self):
        queryset = models.LoanBook.objects.filter(book__owner = self.request.user)
        return queryset
