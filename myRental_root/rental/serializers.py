from rest_framework import serializers
from . import models

class LoanBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanBook
        fields = '__all__'
