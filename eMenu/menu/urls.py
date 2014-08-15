from django.conf.urls import patterns, url

from menu import views

urlpatterns = patterns('',
    url(r'^$', views.wyswietl_menu, name='wyswietl_menu')
)