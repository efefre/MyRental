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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        book_id = request.data['book']
        books_models.Books.objects.filter(id=book_id).update(status='LO')

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        book_id = instance.book.id
        self.perform_destroy(instance)

        books_models.Books.objects.filter(id=book_id).update(status='AV')

        return Response(status=status.HTTP_204_NO_CONTENT)
