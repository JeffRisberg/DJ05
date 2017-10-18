from django.conf.urls import url, include

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^api/events/(?P<pk>[0-9]+)/$',
        views.EventAPIView.as_view(),
        name='event'),

    url(r'^api/events/$',
        views.EventsAPIView.as_view(),
        name='events'),

    url(r'^api/items/(?P<pk>[0-9]+)/$',
        views.ItemAPIView.as_view(),
        name='item'),

    url(r'^api/items/$',
        views.ItemsAPIView.as_view(),
        name='items'),

    url(r'^$', views.IndexView.as_view(), name='index'),
]
