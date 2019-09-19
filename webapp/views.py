from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from webapp.models import Room, Chat
from webapp.serializers import (RoomSerializer, ChatSerializer,
                                ChatPostSerializer)


# Create your views here.


class RoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})


class ChatView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get('room')  # MESHAN
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializer(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # room = request.data.get('room')
        chat = ChatPostSerializer(data=request.data)
        if chat.is_valid():   # MESHAN
            chat.save(user=request.user)  # MESHAN
            return Response({'status': 'Add chat'})
        return Response({'status': 'Error'})
