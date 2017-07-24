from django.conf.urls import url
from . import views

app_name = 'MyApp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'^(?P<post_id>[0-9]+)/item/$', views.item, name='item'),
    url(r'^(?P<post_id>[0-9]+)/user/$', views.user, name='user'),
]