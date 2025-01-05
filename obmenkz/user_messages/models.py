from django.db import models
from django.contrib.auth import get_user_model
from carts.models import Cart

User = get_user_model()

class MessageThread(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="threads_as_buyer"
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="threads_as_seller"
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="threads"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Thread: {self.buyer.username} -> {self.seller.username} ({self.cart.title})"

class Message(models.Model):
    thread = models.ForeignKey(
        MessageThread, on_delete=models.CASCADE, related_name="messages"
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in thread {self.thread.id}"
