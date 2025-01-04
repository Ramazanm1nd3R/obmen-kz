from django.urls import path
from .views import CartListCreateView, CartDetailView, CartImageUploadView

urlpatterns = [
    path('', CartListCreateView.as_view(), name='cart-list-create'),
    path('<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('images/', CartImageUploadView.as_view(), name='cart-image-upload'),
]
