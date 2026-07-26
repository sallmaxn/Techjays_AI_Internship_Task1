# pylint: disable=no-member, maybe-no-member
"""Database models for the ChatGPT Clone."""

from django.db import models
from django.contrib.auth.models import User


class ChatSession(models.Model):
    """Represents an individual conversational thread for a user"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="New Chat")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Message(models.Model):
    """Represents a single message exchange within a chat session."""

    chat = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        content_str = str(self.content)
        return f"{self.role}: {content_str[:30]}"
