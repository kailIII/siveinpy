from django.conf.urls import patterns, include, url
from .views import index, index2

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SiveinPy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apps.inicio.views.index', name='homepage'),
    url(r'^index/$', index2.as_view() ),
)