from rest_framework import serializers
from . import models
from books import models as books_models

class LoanBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LoanBook
        fields = '__all__'

    def validate_book(self, value):
        if self.context['request']:
            user = self.context['request'].user

        if value.owner != user:
            raise serializers.ValidationError('You are not an owner of this book.')

        return value

    def create(self, validated_data):
        book = validated_data['book']
        book_id = book.id

        loan_book = models.LoanBook.objects.create(**validated_data)
        books_models.Books.objects.filter(id=book_id).update(status='LO')

        return loan_book
