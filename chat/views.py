# pylint: disable=no-member, maybe-no-member
"""Views for the ChatGPT Clone application."""

import os
import markdown

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from dotenv import load_dotenv
from openai import OpenAI

from .models import ChatSession, Message

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)


@login_required
def chat_view(request, chat_id=None):
    """Display the chat page and process messages."""
    if chat_id:
        chat = get_object_or_404(ChatSession, id=chat_id, user=request.user)
    else:
        chat, _ = ChatSession.objects.get_or_create(user=request.user, title="New Chat")

    if request.method == "POST":
        user_message = request.POST.get("message")

        if user_message:
            # 1. Save user message to database
            Message.objects.create(chat=chat, role="user", content=user_message)

            # 2. Update Chat Title dynamically if its new

            if chat.title == "New Chat":
                chat.title = user_message[:30]
                chat.save()
            # 3. System prompt archiecture initialization
            history = [
                {
                    "role": "system",
                    "content": """
You are ChatGPT, a professional AI assistant.

Rules:
- Always use Markdown.
- Use headings (##) for sections.
- Use bullet points instead of tables unless the user specifically asks for a table.
- Use **bold** for important words.
- Leave a blank line between sections.
- Keep answers clean, readable, and visually attractive.
- Avoid using the "|" character unless creating a real Markdown table.
- When giving lists, use bullet points.
- Give concise but informative answers.
""",
                }
            ]

            previous_messages = Message.objects.filter(chat=chat).order_by("created_at")

            for msg in previous_messages:
                history.append({"role": msg.role, "content": msg.content})
            response = client.chat.completions.create(
                model="cohere/north-mini-code:free", messages=history
            )

            assistant_reply = response.choices[0].message.content
            assistant_reply = markdown.markdown(
                assistant_reply, extensions=["fenced_code", "tables", "nl2br"]
            )

            Message.objects.create(chat=chat, role="assistant", content=assistant_reply)

            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse(
                    {
                        "success": True,
                        "user_message": user_message,
                        "assistant_reply": assistant_reply,
                        "chat_id": chat.id,
                    }
                )

    messages = Message.objects.filter(chat=chat).order_by("created_at")
    all_chats = ChatSession.objects.filter(user=request.user).order_by("created_at")

    return render(
        request,
        "chat.html",
        {
            "messages": messages,
            "all_chats": all_chats,
            "current_chat": chat,
        },
    )


@login_required
def new_chat(request):
    """Create a new chat session."""
    chat = ChatSession.objects.create(user=request.user, title="New Chat")
    return redirect("chat_detail", chat_id=chat.id)
