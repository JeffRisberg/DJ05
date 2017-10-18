from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url
# from rest_framework.authtoken import views as drf_views


urlpatterns = [
    url(r'^backend/', include('backend.urls', namespace="backend")),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('backend.urls', namespace="backend")),
]