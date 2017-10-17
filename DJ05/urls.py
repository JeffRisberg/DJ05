from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

