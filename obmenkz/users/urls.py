from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    CurrentUserView, 
    UpdateUserProfileView, 
    ChangePasswordView, 
    DeleteAccountView,
    RegisterView,
)

urlpatterns = [
    # Эндпоинт для регистрации
    path('register/', RegisterView.as_view(), name='register'),

    # Эндпоинты для пользователей
    # path('', UserListView.as_view(), name='user-list'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Эндпоинты для аутентификации
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Эндпоинты для взаимодействия с аккаунтом
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('me/update/', UpdateUserProfileView.as_view(), name='update-user-profile'),
    path('me/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('me/delete/', DeleteAccountView.as_view(), name='delete-account'),
]
