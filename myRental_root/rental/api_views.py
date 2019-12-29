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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        book_id = instance.book.id
        self.perform_destroy(instance)

        books_models.Books.objects.filter(id=book_id).update(status='AV')

        return Response(status=status.HTTP_204_NO_CONTENT)
