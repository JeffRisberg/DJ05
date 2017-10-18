from django.contrib import admin

from .models import Event, Item


class EventAdmin(admin.ModelAdmin):
    fields = ('text', 'time', 'completed')
    list_display = ['id', 'text', 'time', 'completed']


admin.site.register(Event, EventAdmin)


class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'value', 'description', 'completed')
    list_display = ['id', 'name', 'value', 'description', 'completed']


admin.site.register(Item, ItemAdmin)
