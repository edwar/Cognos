from django.contrib.auth import logout, login as auth_login
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render


class InicioView(TemplateView):
    template_name = 'inicio.html'

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/analisis/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class LandingView(TemplateView):
    template_name = 'analisis.html'

class ExcelCreate(TemplateView):
    template_name = 'carga.html'


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/analisis/inicio/')
        return render(request, 'inicio.html',{'msg':'Error'})
    else:
        return HttpResponseRedirect('/analisis/')