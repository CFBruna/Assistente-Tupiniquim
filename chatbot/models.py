from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.conversation.user.username}: {self.message}'
