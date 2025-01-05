from django.contrib import admin
from .models import MessageThread, Message

@admin.register(MessageThread)
class MessageThreadAdmin(admin.ModelAdmin):
    list_display = ("id", "buyer", "seller", "cart")
    search_fields = ("buyer__username", "seller__username", "cart__title")
    list_filter = ("buyer", "seller")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "thread", "sender", "text", "is_read", "created_at")
    search_fields = ("thread__buyer__username", "thread__seller__username", "text")
    list_filter = ("is_read", "created_at")
