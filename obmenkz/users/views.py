from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser
from .serializers import CustomUserSerializer, RegistrationSerializer


# Получение данных о текущем пользователе
class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get current user profile",
        operation_description="Retrieve the profile of the currently authenticated user.",
        responses={200: CustomUserSerializer}
    )
    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Обновление профиля пользователя
class UpdateUserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Update user profile",
        operation_description="Update profile details like username, email, or phone number.",
        request_body=CustomUserSerializer,
        responses={200: "Profile updated successfully", 400: "Validation error"}
    )
    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Смена пароля
class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Change password",
        operation_description="Change the password of the currently authenticated user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'old_password': openapi.Schema(type=openapi.TYPE_STRING, description='Current password'),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING, description='New password'),
            },
            required=['old_password', 'new_password']
        ),
        responses={
            200: "Password updated successfully",
            400: "Validation error or incorrect old password"
        }
    )
    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        # Проверяем старый пароль
        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем валидность нового пароля
        try:
            validate_password(new_password, user=user)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        # Обновляем пароль
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)


# Удаление аккаунта
class DeleteAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Delete account",
        operation_description="Delete the currently authenticated user's account.",
        responses={204: "Account deleted successfully"}
    )
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class RegisterView(APIView):
    @swagger_auto_schema(
        operation_summary="Register a new user",
        operation_description="Endpoint for user registration. Accepts username, email, and password.",
        request_body=RegistrationSerializer,
        responses={
            201: "User registered successfully.",
            400: "Validation error."
        }
    )
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)