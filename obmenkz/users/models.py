from django.db.models import Avg
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    average_rating = models.FloatField(default=0.0)

    def calculate_average_rating(self):
        from reviews.models import Review
        avg_rating = Review.objects.filter(user=self).aggregate(avg=models.Avg('rating'))['avg']
        if avg_rating is not None:
            self.average_rating = round(avg_rating, 2)  # Округляем до 2-х знаков
        else:
            self.average_rating = 0.0
        self.save()

    def __str__(self):
        return self.username
