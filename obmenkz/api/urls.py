from django.urls import path, include

urlpatterns = [
    path('carts/', include('carts.urls')),  # Эндпоинты для объявлений
    path('reviews/', include('reviews.urls')),  # Эндпоинты для отзывов
    path('users/', include('users.urls')),  # Эндпоинты для пользователей
    path('user-messages/', include('user_messages.urls')),  # Эндпоинты для сообщений
]
