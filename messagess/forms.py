from django import forms
from .models import Message


class sendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['to_who', 'title', 'text', ]
