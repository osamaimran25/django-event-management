from typing import List, Any

from django.core.paginator import Paginator
from rest_framework import serializers

from events.models import Event
from events.pagination import AttendeePagination
from event_management.users.api.serializers import UserSerializer
from event_management.users.models import User


class EventSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'owner']


class EventAttendeeSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    attendees = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'owner', 'attendees']

    def get_attendees(self, obj: Event) -> Any:
        attendee_page_size = self.context['request'].query_params.get('attendee_page_size', 20)
        attendees = obj.attendees.all()
        if not attendees:
            return []
        paginator = AttendeePagination()
        page = paginator.paginate_queryset(attendees, self.context['request'])
        serializer = UserSerializer(page, many=True)
        return serializer.data
