from django.db import models


class Event(models.Model):
    text = models.TextField()
    time = models.IntegerField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return self.text


class Item(models.Model):
    name = models.TextField()
    value = models.IntegerField()
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name