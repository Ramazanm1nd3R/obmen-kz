from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Cart, CartImage
from .serializers import CartSerializer, CartImageUploadSerializer
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Вы авторизованы!"})

# Список объявлений и создание нового
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Get list of all carts",
        operation_description="Retrieve a list of all carts with optional filters.",
        responses={200: CartSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new cart",
        operation_description="Create a new cart. Requires authentication.",
        responses={201: CartSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Детали объявления, обновление и удаление
class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Retrieve cart details",
        operation_description="Get detailed information about a specific cart by ID.",
        responses={200: CartSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a cart",
        operation_description="Update the details of a specific cart. Requires authentication.",
        responses={200: CartSerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a cart",
        operation_description="Delete a specific cart. Requires authentication.",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise PermissionError("You can only edit your own carts.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionError("You can only delete your own carts.")
        instance.delete()


# Загрузка изображения для объявления
class CartImageUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Upload an image for a cart",
        operation_description="Upload an image associated with a specific cart. Requires authentication.",
        request_body=CartImageUploadSerializer,
        responses={201: CartImageUploadSerializer},
    )
    def post(self, request):
        serializer = CartImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
