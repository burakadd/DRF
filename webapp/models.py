from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User
# Create your models here.


class Room(models.Model):
    creator = models.ForeignKey(
        User,
        verbose_name='Creator',
        on_delete=models.CASCADE
    )

    invited = models.ManyToManyField(
        User,
        verbose_name='Collaborator',
        related_name='invited_user'
    )

    date = models.DateField(
        'Creation date',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Chat Room'
        verbose_name_plural = 'Chat Rooms'


class Chat(models.Model):
    room = models.ForeignKey(
        Room,
        verbose_name='Chat Room',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        verbose_name='User',
        on_delete=models.CASCADE
    )

    text = models.TextField(
        'Message',
        max_length=500
    )

    date = models.DateTimeField(
        'Send Date',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'
