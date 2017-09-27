from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^tick', views.tick, name='tick'),
    url(r'^$', views.index, name='index'),
]
