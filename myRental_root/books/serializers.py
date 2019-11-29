from rest_framework import serializers
from . import models

class BooksSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault
    )

    class Meta:
        model = models.Books
        fields = '__all__'
