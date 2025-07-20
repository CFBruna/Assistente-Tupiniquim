from django.http import JsonResponse
from django.shortcuts import render
from chatbot.models import Chat


def chatbot(request):
    chats = Chat.objects.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        response = message
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})
