from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, SupportTicket


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class SupportTicketForm(forms.ModelForm):
    CHOICES = (
        (1, 'Error'),
        (2, 'Forum'),
        (3, 'Others'),
        (4, 'Violation of the rules '),
        (5, 'Premium'),
        (6, 'Registration problems'),
        (7, 'Question'),
    )

    question_type = forms.ChoiceField(label="", initial='', widget=forms.Select, choices=CHOICES, required=True)

    class Meta:
        model = SupportTicket
        fields = ['text']


class UniqueUserEmailField(forms.EmailField):
    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already exists")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass


class ExtendedUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=30)
    email = UniqueUserEmailField(required=True, label='Email address')
    first_name = forms.CharField(required=False, max_length=30)
    last_name = forms.CharField(required=False, max_length=30)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['email', 'first_name', 'last_name',
                                'password1', 'password2']

    def clean(self, *args, **kwargs):
        cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
        return cleaned_data

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit)
        if user:
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
        return user
