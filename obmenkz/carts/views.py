from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartImage
from .serializers import CartSerializer, CartImageUploadSerializer

# Список объявлений и создание нового
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Детали объявления, обновление и удаление
class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

    def post(self, request):
        serializer = CartImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
