from django.db import models
from django import forms


class Message(models.Model):
    username = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
