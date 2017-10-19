from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView, RetrieveAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Event, Item
from .serializers import EventSerializer, ItemSerializer


class IndexView(TemplateView):
    template_name = 'backend/index.html'


class EventAPIView(RetrieveAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_object(self):
        return get_object_or_404(Event, id=self.kwargs['pk'])


class EventsAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ItemAPIView(RetrieveAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_object(self):
        return get_object_or_404(Item, id=self.kwargs['pk'])


class ItemsAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
