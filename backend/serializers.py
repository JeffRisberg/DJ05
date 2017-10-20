from rest_framework import serializers

from .models import Event, Item


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id',
                  'text', 'time', 'completed', 'updated_at')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id',
                  'name', 'value', 'description', 'completed', 'updated_at')
