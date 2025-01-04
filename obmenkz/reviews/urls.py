from django.urls import path
from .views import ReviewListCreateView

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:user_id>/', ReviewListCreateView.as_view(), name='user-reviews'),
]
