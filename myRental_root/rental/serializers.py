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
