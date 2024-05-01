
from django.db import models
from typing import List
from datetime import datetime
from event_management.users.models import User


class Event(models.Model):
    title: str = models.CharField(max_length=255)
    description: str = models.TextField()
    date: datetime = models.DateTimeField()
    location:str = models.CharField(max_length=255)
    owner: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_event')
    attendees: List[User] = models.ManyToManyField(User, related_name='attended_events')

    class Meta:
        app_label = 'events'
