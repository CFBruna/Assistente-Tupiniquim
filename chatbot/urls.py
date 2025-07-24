from django.urls import path
from . import views


urlpatterns = [
    path('', views.ChatHistoryListView.as_view(), name='chat_history'),
    path('chatbot/new/', views.create_new_chat, name='create_new_chat'),
    path('chatbot/<int:pk>/', views.chatbot, name='chatbot'),
    path('conversation/<int:pk>/rename/', views.rename_conversation, name='rename_conversation'),
]
