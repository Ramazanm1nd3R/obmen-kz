from rest_framework import serializers
from .models import Cart, CartImage

class CartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartImage
        fields = ['id', 'image', 'uploaded_at']


class CartSerializer(serializers.ModelSerializer):
    images = CartImageSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'title', 'description', 'price', 'category', 'created_at', 'updated_at', 'images']
        read_only_fields = ['user', 'created_at', 'updated_at']


class CartImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartImage
        fields = ['image', 'cart']
