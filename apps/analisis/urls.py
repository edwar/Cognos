from django.conf.urls import url
from .views import InicioView, login, LandingView, LogoutView, ExcelCreate

urlpatterns = [
    url(r'^$', InicioView.as_view(), name='inicio'),
    url(r'^login/$', login, name='login'),
    url(r'^inicio/$', LandingView.as_view()),
    url(r'^salir/$', LogoutView.as_view()),
    url(r'^cargar/$', ExcelCreate.as_view()),
]
