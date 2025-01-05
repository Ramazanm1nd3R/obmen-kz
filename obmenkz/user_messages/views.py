from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import MessageThread, Message
from .serializers import MessageThreadSerializer, MessageSerializer


# Список и создание диалогов
class MessageThreadListCreateView(generics.ListCreateAPIView):
    queryset = MessageThread.objects.all()
    serializer_class = MessageThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get message threads",
        operation_description="Retrieve all message threads of the current user.",
        responses={200: MessageThreadSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new message thread",
        operation_description="Create a new thread for a specific cart between a buyer and seller.",
        request_body=MessageThreadSerializer,
        responses={
            201: "Thread created successfully.",
            400: "Validation error.",
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        return MessageThread.objects.filter(
            buyer=self.request.user
        ) | MessageThread.objects.filter(seller=self.request.user)


# Список сообщений в диалоге
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get messages in a thread",
        operation_description="Retrieve all messages from a specific thread.",
        manual_parameters=[
            openapi.Parameter(
                'thread_id',
                openapi.IN_PATH,
                description="ID of the thread",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={200: MessageSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        thread_id = self.kwargs.get('thread_id')
        return Message.objects.filter(thread_id=thread_id)


# Создание сообщения
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Send a message",
        operation_description="Send a new message in a specific thread.",
        request_body=MessageSerializer,
        responses={
            201: "Message sent successfully.",
            400: "Validation error.",
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        thread = serializer.validated_data['thread']
        if self.request.user != thread.buyer and self.request.user != thread.seller:
            raise PermissionError("You can only send messages in your own threads.")
        serializer.save(sender=self.request.user)


# Отметка сообщения как прочитанного
class MarkMessageAsReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Mark message as read",
        operation_description="Mark a specific message as read.",
        manual_parameters=[
            openapi.Parameter(
                'message_id',
                openapi.IN_PATH,
                description="ID of the message",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={
            200: "Message marked as read successfully.",
            404: "Message not found.",
        }
    )
    def post(self, request, message_id):
        try:
            message = Message.objects.get(id=message_id)
            if message.thread.buyer != request.user and message.thread.seller != request.user:
                return Response({"error": "You can only mark messages in your own threads."}, status=403)
            message.is_read = True
            message.save()
            return Response({"status": "Message marked as read"})
        except Message.DoesNotExist:
            return Response({"error": "Message not found."}, status=404)
