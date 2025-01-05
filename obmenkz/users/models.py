from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)  # Поле email обязательно и уникально
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Поле для номера телефона
    average_rating = models.FloatField(default=0.0)  # Средний рейтинг пользователя

    def calculate_average_rating(self):
        # Метод для вычисления среднего рейтинга
        from reviews.models import Review  # Импортируем модель Review, чтобы избежать цикличности
        avg_rating = Review.objects.filter(user=self).aggregate(average=Avg('rating'))['average']
        self.average_rating = round(avg_rating, 2) if avg_rating else 0.0
        self.save()

    def __str__(self):
        return self.username
