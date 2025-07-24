import os
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from langchain_groq import ChatGroq
from markdown import markdown
from chatbot.models import Chat, Conversation


os.environ['GROQ_API_KEY'] = settings.GROQ_API_KEY


def get_chat_history(chats):
    chat_history = []
    for chat in chats:
        chat_history.append(
            ('human', chat.message,)
        )
        chat_history.append(
            ('ai', chat.response,)
        )
    return chat_history


def ask_ai(context, message):
    model = ChatGroq(model='llama-3.3-70b-versatile')
    messages = [
        (
            'system',
            'Você é um assistente responsável por tirar dúvidas sobre programação.'
            'Responda em formato markdown'
        ),
    ]
    messages.extend(context)
    messages.append(
        (
            'human',
            message,
        ),
    )
    print(messages)
    response = model.invoke(messages)
    return markdown(response.content, output_format='html')


@login_required
def chatbot(request, pk):
    conversation = Conversation.objects.get(pk=pk)
    chats = Chat.objects.filter(conversation=conversation)

    if request.method == 'POST':
        context = get_chat_history(
            chats=chats,
        )
        message = request.POST.get('message')
        response = ask_ai(
            context=context,
            message=message,
        )

        chat = Chat(
            conversation=conversation,
            message=message,
            response=response,
        )
        chat.save()

        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})


class ChatHistoryListView(LoginRequiredMixin, ListView):
    model = Conversation
    template_name = 'chat_history.html'

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)


@login_required
def create_new_chat(request):
    new_conversation = Conversation.objects.create(
        user=request.user,
        title='Nova Conversa',
    )
    return redirect(reverse('chatbot', kwargs={'pk': new_conversation.pk}))


@login_required
def rename_conversation(request, pk):
    if request.method == 'POST':
        try:
            conversation = Conversation.objects.get(pk=pk, user=request.user)
            new_title = request.POST.get('title')

            if new_title:
                conversation.title = new_title
                conversation.save()
                return JsonResponse({'status': 'success', 'new_title': conversation.title})
            else:
                return JsonResponse({'status': 'error', 'message': 'O título não pode ficar em branco.'}, status=400)
        except Conversation.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Conversa não encontrada.'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Método de requisição inválido.'}, status=405)


@login_required
def delete_conversation(request, pk):
    if request.method == 'POST':
        try:
            conversation = Conversation.objects.get(pk=pk, user=request.user)
            conversation.delete()
            return JsonResponse({'status': 'success', 'message': 'Conversa removida com sucesso.'})

        except Conversation.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Conversa não encontrada.'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Método de requisição inválido.'}, status=405)
