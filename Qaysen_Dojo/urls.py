from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),

	# Pagina de Inicio
	url(r'^$', 'principal.views.inicio'),

	# Lista de Cursos
	url(r'^cursos/$', 'principal.views.lista_cursos'),

	url(r'^cursos/$','principal.views.cursos'),
	url(r'^cursos/(?P<id_curso_ab>\d+)$','principal.views.dato_curso_abierto'),
)


