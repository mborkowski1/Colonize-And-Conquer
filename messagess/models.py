from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    to_who = models.ForeignKey(User, on_delete=models.CASCADE)
    have_seen = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
