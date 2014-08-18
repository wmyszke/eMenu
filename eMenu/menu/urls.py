from django.conf.urls import patterns, url

from menu import views

urlpatterns = patterns('',
    url(r'^$', views.wyswietl_menu, name='wyswietl_menu'),
    url(r',n$', views.wyswietl_po_nazwie, name='wyswietl_po_nazwie'),
    url(r',i$', views.wyswietl_menu_po_ilosci_dan, name='wyswietl_menu_po_ilosci_dan'),
    url(r'^karta/(?P<menu_id>\d+)/$', views.menu_details, name='menu_details'),
    url(r'^blad/$', views.blad, name='blad'),
)