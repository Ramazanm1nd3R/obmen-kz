from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Retrieve a list of users",
        operation_description="Fetch all users or filter them if necessary.",
        manual_parameters=[
            openapi.Parameter(
                'ordering', openapi.IN_QUERY, 
                description="Order users by fields (e.g., `username`, `average_rating`). Prefix with `-` for descending order.", 
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'search', openapi.IN_QUERY, 
                description="Search users by username or email.", 
                type=openapi.TYPE_STRING
            ),
        ],
        responses={200: CustomUserSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Retrieve a specific user by ID",
        operation_description="Fetch detailed information about a user, including their ratings and contact information.",
        responses={
            200: CustomUserSerializer,
            404: "Not Found: User with the specified ID does not exist."
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
