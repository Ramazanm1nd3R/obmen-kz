from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # Или можно сделать отдельную модель категорий
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CartImage(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cart_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
