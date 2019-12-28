from rest_framework import viewsets

from . import models
from . import serializers

class LoanBookViewset(viewsets.ModelViewSet):
    serializer_class = serializers.LoanBookSerializer
    queryset = models.LoanBook.objects.all()
