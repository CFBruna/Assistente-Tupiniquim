import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from langchain_groq import ChatGroq
from markdown import markdown
from chatbot.models import Chat


os.environ['GROQ_API_KEY'] = settings.GROQ_API_KEY


def ask_ai(message):
    model = ChatGroq(model='llama-3.3-70b-versatile')
    message = [
        (
            'system',
            'Você é um assistente responsável por tirar dúvidas sobre programação.'
            'Responda em formato markdown'
        ),
        (
            'human',
            message,
        ),
    ]
    response = model.invoke(message)
    return markdown(response.content, output_format='html')


def chatbot(request):
    chats = Chat.objects.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_ai(message)
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})
