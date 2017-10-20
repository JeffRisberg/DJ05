import time

from rest_framework import serializers

from .models import Event, Item


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))


class EventSerializer(serializers.HyperlinkedModelSerializer):
    date_created = TimestampField() #Source must be a models.DateTimeField
    last_updated = TimestampField() #Source must be a models.DateTimeField

    class Meta:
        model = Event
        fields = ('id',
                  'text', 'time', 'completed', 'date_created', 'last_updated')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    date_created = TimestampField() #Source must be a models.DateTimeField
    last_updated = TimestampField() #Source must be a models.DateTimeField

    class Meta:
        model = Item
        fields = ('id',
                  'name', 'value', 'description', 'completed', 'date_created', 'last_updated')
