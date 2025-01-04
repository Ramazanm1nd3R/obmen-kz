from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Review
from .serializers import ReviewSerializer
from carts.models import Cart

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Описание параметров запроса для получения отзывов о пользователе
    @swagger_auto_schema(
        operation_summary="List reviews",
        operation_description="Retrieve all reviews or reviews for a specific user by user ID.",
        manual_parameters=[
            openapi.Parameter(
                "user_id", openapi.IN_QUERY, 
                description="ID of the user to filter reviews", 
                type=openapi.TYPE_INTEGER, 
                required=False
            ),
        ],
        responses={200: ReviewSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Описание параметров запроса для создания отзыва
    @swagger_auto_schema(
        operation_summary="Create a review",
        operation_description="Create a new review for a specific transaction (cart). Requires authentication.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "cart": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the cart (transaction)"),
                "rating": openapi.Schema(type=openapi.TYPE_INTEGER, description="Rating from 1 to 5"),
                "comment": openapi.Schema(type=openapi.TYPE_STRING, description="Optional comment"),
            },
            required=["cart", "rating"]
        ),
        responses={
            201: openapi.Response("Review created successfully", ReviewSerializer),
            400: "Bad Request: Invalid data or permissions error"
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            return Review.objects.filter(user_id=user_id)
        return Review.objects.all()

    def perform_create(self, serializer):
        cart = serializer.validated_data['cart']
        if cart.user != self.request.user:  # Проверяем, является ли текущий пользователь покупателем
            raise PermissionError("You can only leave reviews for your own transactions.")
        serializer.save(author=self.request.user, user=cart.user)
