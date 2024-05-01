from rest_framework import serializers
from events.models import Event
from event_management.users.api.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'owner']