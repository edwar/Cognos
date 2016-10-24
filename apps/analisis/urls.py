from django.conf.urls import url
from .views import InicioView, login, LandingView, LogoutView, ExcelCreate, ArchivoView, UsuariosList, TodoView, DetalleView, EtlView, GraficaView

urlpatterns = [
    url(r'^$', InicioView.as_view(), name='inicio'),
    url(r'^login/$', login, name='login'),
    url(r'^inicio/$', LandingView.as_view()),
    url(r'^salir/$', LogoutView.as_view()),
    url(r'^cargar/$', ExcelCreate.as_view()),
    url(r'^archivos/$', ArchivoView.as_view()),
    url(r'^usuarios/$', UsuariosList.as_view()),
    url(r'^etl/$', EtlView.as_view()),
    url(r'^todo/$', TodoView.as_view()),
    url(r'^grafica/$', GraficaView.as_view()),
    url(r'^detalle/(?P<archivo>[\w\-]+)/(?P<usuario>[\w\-]+)/$', DetalleView.as_view()),
]
