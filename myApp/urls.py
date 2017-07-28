from django.conf.urls import url
from . import views

app_name = 'MyApp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'user/item/(?P<itemNum>[0-9]+)/$', views.details, name='details'),
    url(r'filter/condition/(?P<filterNum>[0-9]+)/$', views.filterCon, name='filterC'),
    url(r'filter/type/(?P<filterNum>[0-9]+)/$', views.filterType, name='filterT'),
    url(r'(?P<itemNum>[0-9]+)/$', views.details, name='details'),
    url(r'item/(?P<itemNum>[0-9]+)/$', views.details, name='details'),  
    
   # url(r'^user/(?P<user_id>[0-9]+)/$')
   
#    url(r'^tags/$', 'blog.views.tags'),
#    url(r'^tag/(?P[-_A-Za-z0-9]+)/$','blog.views.with_tag'),
#    url(r'^tag/(?P[-_A-Za-z0-9]+)/page/(?Pd+)/$', 'blog.views.with_tag' ),
]