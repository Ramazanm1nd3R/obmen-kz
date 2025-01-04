from django.db import models
from django.contrib.auth import get_user_model
from carts.models import Cart  # Импортируем модель объявления (Cart)

User = get_user_model()

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_written")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_received")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField()  # Рейтинг от 1 до 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author.username} for {self.user.username} - {self.rating}/5"

    class Meta:
        unique_together = ('author', 'cart')  # Один отзыв на сделку
