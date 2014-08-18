from django.conf.urls import patterns, include, url

from django.contrib import admin

# only for development, do not use in prod
from django.conf import settings
from django.conf.urls.static import static 

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eMenu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'', include('menu.urls')),
    url(r',n$', include('menu.urls')),
    url(r',i$', include('menu.urls')),
    url(r'/karta/', include('menu.urls')),
    url(r'/blad/$', include('menu.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # only for development, do not use in prod
