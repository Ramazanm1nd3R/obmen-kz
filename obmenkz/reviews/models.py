from django.core.exceptions import ValidationError
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
        choices=[(i, i) for i in range(1, 6)],  # Рейтинг от 1 до 5
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

    def clean(self):
        # Проверка: пользователь не может оставить отзыв самому себе
        if self.author == self.user:
            raise ValidationError("You cannot leave a review for yourself.")

        # Проверка: пользователь может оставлять отзывы только на товары других пользователей
        if self.cart.user == self.author:
            raise ValidationError("You cannot leave a review for your own cart.")

        # Проверка: один отзыв на товар
        if Review.objects.filter(author=self.author, cart=self.cart).exists():
            raise ValidationError("You have already left a review for this cart.")

    def save(self, *args, **kwargs):
        self.clean()  # Вызываем clean() перед сохранением
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review by {self.author.username} for {self.user.username} - {self.rating}/5"

    class Meta:
        unique_together = ('author', 'cart')  # Один отзыв на одну сделку
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']  # Сортировка: сначала новые отзывы
