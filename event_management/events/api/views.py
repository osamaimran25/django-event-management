from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from events.models import Event
from events.pagination import EventPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, EventAttendeeSerializer


class EventManagement(APIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_object(self, pk: int) -> Event:
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk: int) -> Response:
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def post(self, request) -> Response:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int) -> Response:
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int, format=None) -> Response:
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventList(generics.ListAPIView):
    permission_classes: Any = (AllowAny,)
    queryset: Any = Event.objects.all()
    serializer_class: Any = EventAttendeeSerializer
    pagination_class: Any = EventPagination


class AttendEvent(APIView):
    permission_classes = (IsAuthenticated, )

    def get_event(self, event_id: int) -> Event:
        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise Http404

    def post(self, request, event_id: int) -> Response:
        event = self.get_event(event_id)
        if event.attendees.filter(id=request.user.id).exists():
            return Response({"message": "You are already attending this event."}, status=status.HTTP_400_BAD_REQUEST)
        elif request.user == event.owner:
            return Response({"message": "Owner can not be attendee."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            event.attendees.add(request.user)
            return Response({"message": "You have successfully attended the event."}, status=status.HTTP_201_CREATED)