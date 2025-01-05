from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()  # Поле доступно только для чтения

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'average_rating']
