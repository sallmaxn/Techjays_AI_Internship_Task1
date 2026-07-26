"""URL patterns for chat app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_view, name="chat"),
    path("<int:chat_id>/", views.chat_view, name="chat_detail"),
    path("new/", views.new_chat, name="new_chat"),
]
