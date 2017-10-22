from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import renderers
from rest_framework.generics import (
    ListAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Event, Item
from .serializers import EventSerializer, ItemSerializer


class CustomRenderer(renderers.JSONRenderer):
    """
    Renderer which serializes to CustomXML.
    """

    def render(self, data, accepted_media_type=None, render_context=None):
        response = render_context['response']

        if data == None:
            data = {'status': 'ok'}
        elif 'results' in data:
            data = {'count': data.get('count', None),
                    'next': data.get('next', None),
                    'previous': data.get('previous', None),
                    'data': data.get('results')}
        elif 'detail' in data:
            data = {'status': data.get('detail')}
        else:
            data = {'status': 'ok', 'data': data}

        return super(CustomRenderer, self).render(data, accepted_media_type, render_context)


class IndexView(TemplateView):
    template_name = 'backend/index.html'


class EventAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer
    renderer_classes = [CustomRenderer]

    def get_object(self):
        return get_object_or_404(Event, id=self.kwargs['pk'])


class EventsAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    renderer_classes = [CustomRenderer]


class ItemAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    renderer_classes = [CustomRenderer]

    def get_object(self):
        return get_object_or_404(Item, id=self.kwargs['pk'])


class ItemsAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    renderer_classes = [CustomRenderer]
