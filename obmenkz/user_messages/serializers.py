from rest_framework import serializers
from .models import MessageThread, Message

class MessageThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageThread
        fields = ['id', 'buyer', 'seller', 'cart', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'thread', 'sender', 'text', 'is_read', 'created_at']
