from django.contrib import admin
from .models import MessageThread, Message

@admin.register(MessageThread)
class MessageThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'seller', 'cart', 'created_at')
    search_fields = ('buyer__username', 'seller__username', 'cart__title')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'sender', 'text', 'is_read', 'created_at')
    search_fields = ('thread__id', 'sender__username', 'text')
    list_filter = ('is_read', 'created_at')
