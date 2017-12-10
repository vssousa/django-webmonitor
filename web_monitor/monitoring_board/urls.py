from django.conf.urls import url

from . import views

app_name = 'monitoring_board'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pages/(?P<contact_id>[0-9]+)$', views.pages, name='pages'),
    url(r'^add/contact$', views.addContact, name='add_contact'),
    url(r'^add/page$', views.addPage, name='add_page'),
]