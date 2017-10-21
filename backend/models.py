from django.db import models


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(BaseModel):
    text = models.TextField()
    time = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return self.text


class Item(BaseModel):
    name = models.TextField()
    value = models.IntegerField()
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
