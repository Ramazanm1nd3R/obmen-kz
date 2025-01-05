from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review

@receiver(post_save, sender=Review)
def update_user_rating(sender, instance, **kwargs):
    user = instance.user
    user.calculate_average_rating()
