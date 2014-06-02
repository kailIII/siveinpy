from django.conf.urls import patterns, include, url
from .views import RegistrarAutor, MostrarAutor

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SiveinPy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^registrar/$',RegistrarAutor.as_view(), name="registrar_autor"),
    url(r'^mostrar/$',MostrarAutor.as_view(), name="mostrar_autor"),
)
