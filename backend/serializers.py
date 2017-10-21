import time

import datetime

from rest_framework import serializers

from .models import Event, Item


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))
    def to_internal_value(self, value):
        return datetime.datetime.fromtimestamp(value)


class EventSerializer(serializers.ModelSerializer):
    date_created = TimestampField() #Source must be a models.DateTimeField
    last_updated = TimestampField() #Source must be a models.DateTimeField

    class Meta:
        model = Event
        fields = ('id',
                  'text', 'time', 'completed', 'date_created', 'last_updated')


class ItemSerializer(serializers.ModelSerializer):
    date_created = TimestampField() #Source must be a models.DateTimeField
    last_updated = TimestampField() #Source must be a models.DateTimeField

    class Meta:
        model = Item
        fields = ('id',
                  'name', 'value', 'description', 'completed', 'date_created', 'last_updated')
