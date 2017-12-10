from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<update>[0-1]+)$', views.home, name='home'),
    url(r'^contact/(?P<update>[0-1]+)$', views.contact, name='contact'),
    url(r'^contact/(?P<update>[0-1]+)/(?P<contact_id>[0-9]+)$', views.contactInfo, name='contact_info'),
    url(r'^about/(?P<update>[0-1]+)$', views.about, name='about'),
    url(r'^price/(?P<update>[0-1]+)$', views.price, name='price'),
]
