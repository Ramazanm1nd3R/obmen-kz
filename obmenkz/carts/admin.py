from django.contrib import admin
from .models import Cart, CartImage

# Регистрация модели Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'price', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)

# Регистрация модели CartImage
@admin.register(CartImage)
class CartImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'image', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('cart__title',)
    ordering = ('-uploaded_at',)
