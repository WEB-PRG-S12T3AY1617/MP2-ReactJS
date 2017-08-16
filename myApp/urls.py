from django.conf.urls import url
from . import views

app_name = 'MyApp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'user/item/(?P<itemNum>[0-9]+)/$', views.details, name='details'),
    url(r'filter/condition/(?P<filterNum>[0-9]+)/$', views.filterCon, name='filterC'),
    url(r'filter/type/(?P<filterNum>[0-9]+)/$', views.filterType, name='filterT'),
    url(r'(?P<itemNum>[0-9]+)/$', views.details, name='details'),
    url(r'item/(?P<itemNum>[0-9]+)/$', views.details, name='details'),
    url(r'^upload/$', views.upload_file, name='upload'),
    url(r'offer/', views.OfferView.as_view(), name='MakeOffer'),
    url(r'offer/$', views.OfferView.as_view(), name='MakeOffer'),
    url(r'^user/(?P<user_id>[0-9]+)/seeOffer/', views.seeOffer, name='seeOffer'),
    url(r'^view/accept/', views.offerAccept, name='offerAccept'),
    url(r'^view/reject/', views.offerReject, name='offerReject'),
]
