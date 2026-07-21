"""Tests for chat app."""

from types import SimpleNamespace
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ChatSession, Message


class ChatTests(TestCase):
    """Test cases for chat application."""

    def setUp(self):
        """Create test user."""
        self.user = User.objects.create_user(
            username="salman",
            password="test12345",
        )

        self.client.login(
            username="salman",
            password="test12345",
        )

    def test_create_chat_session(self):
        """Test chat session creation."""
        chat = ChatSession.objects.create(
            user=self.user,
            title="Test Chat",
        )

        self.assertEqual(chat.title, "Test Chat")
        self.assertEqual(chat.user, self.user)

    def test_create_message(self):
        """Test message creation."""
        chat = ChatSession.objects.create(
            user=self.user,
            title="Test Chat",
        )

        message = Message.objects.create(
            chat=chat,
            role="user",
            content="Hello",
        )

        self.assertEqual(message.role, "user")
        self.assertEqual(message.content, "Hello")

    def test_chat_requires_login(self):
        """Chat page requires authentication."""
        self.client.logout()

        response = self.client.get(reverse("chat"))

        self.assertEqual(response.status_code, 302)

    def test_new_chat(self):
        """New chat endpoint creates chat."""
        response = self.client.get(reverse("new_chat"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ChatSession.objects.count(), 1)

    @patch("chat.views.client.chat.completions.create")
    def test_send_message(self, mock_create):
        """Test sending a message."""

        mock_create.return_value = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content="Hello from AI"
                    )
                )
            ]
        )

        response = self.client.post(
            reverse("chat"),
            {
                "message": "Hi AI"
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.count(), 2)

        self.assertTrue(
            Message.objects.filter(role="user").exists()
        )

        self.assertTrue(
            Message.objects.filter(role="assistant").exists()
        )

    @patch("chat.views.client.chat.completions.create")
    def test_chat_title_updates(self, mock_create):
        """Title updates after first message."""

        mock_create.return_value = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content="AI Reply"
                    )
                )
            ]
        )

        self.client.post(
            reverse("chat"),
            {
                "message": "Python Basics"
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        chat = ChatSession.objects.first()

        self.assertEqual(chat.title, "Python Basics")