from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mainPage.views import main_page
from .models import Message
from .forms import sendMessageForm
# Create your views here.


@login_required(login_url=main_page)
def messages_page(request):
    messages = Message.objects.filter(to_who=request.user).order_by('created_date')
    return render(request, 'indexMessagess.html', {'messages': messages})


@login_required(login_url=main_page)
def messages_detail_page(request, id_of_message):
    message = Message.objects.get(id=id_of_message)
    message.have_seen = True
    message.save()
    return render(request, 'messagessDetail.html', {'message': message})


@login_required(login_url=main_page)
def messages_your_send_page(request):
    messages = Message.objects.filter(author=request.user).order_by('created_date')
    return render(request, 'messagessYourSend.html', {'messages': messages})


@login_required(login_url=main_page)
def messages_send_page(request):
    user = request.user
    if request.method == 'POST':
        messageFormReceived = sendMessageForm(request.POST)
        if messageFormReceived.is_valid():
            message = messageFormReceived.save(commit=False)
            message.author = user
            message.save()
        else:
            return render(request, 'messagessSend.html', {'message_form': messageFormReceived})
    message_form = sendMessageForm()
    return render(request, 'messagessSend.html', {'message_form': message_form})
