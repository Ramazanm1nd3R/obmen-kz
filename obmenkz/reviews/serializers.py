from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Показывает username автора
    user = serializers.StringRelatedField(read_only=True)  # Показывает username получателя

    class Meta:
        model = Review
        fields = ['id', 'author', 'user', 'cart', 'rating', 'comment', 'created_at']
        read_only_fields = ['author', 'user', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def validate(self, data):
        if data['author'] == data['user']:
            raise serializers.ValidationError("You cannot leave a review for yourself.")
        return data
