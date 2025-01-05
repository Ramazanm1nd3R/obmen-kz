from django.urls import path
from .views import (
    MessageThreadListCreateView,
    MessageListView,
    MessageCreateView,
    MarkMessageAsReadView
)

urlpatterns = [
    path('threads/', MessageThreadListCreateView.as_view(), name='message-thread-list'),
    path('threads/<int:thread_id>/messages/', MessageListView.as_view(), name='message-list'),
    path('messages/', MessageCreateView.as_view(), name='message-create'),
    path('messages/<int:message_id>/read/', MarkMessageAsReadView.as_view(), name='message-mark-read'),
]
