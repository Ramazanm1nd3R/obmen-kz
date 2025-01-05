from django.db import models
from django.contrib.auth import get_user_model
from carts.models import Cart  # Импортируем модель объявления (Cart)

User = get_user_model()

class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews_written",
        verbose_name="Author of the review"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews_received",
        verbose_name="User being reviewed"
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Associated Cart"
    )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],  # Выбор из значений от 1 до 5
        verbose_name="Rating (1 to 5)"
    )
    comment = models.TextField(
        blank=True,
        verbose_name="Review comment"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creation"
    )

    def __str__(self):
        return f"Review by {self.author.username} for {self.user.username} - {self.rating}/5"

    class Meta:
        unique_together = ('author', 'cart')  # Один отзыв на одну сделку
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']  # Сортировка: сначала новые отзывы
