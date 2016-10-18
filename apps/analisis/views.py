from django.contrib.auth import logout, login as auth_login
from django.views.generic import RedirectView, TemplateView, CreateView, View, ListView
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Excel, Archivo
from django.contrib.auth.models import User
import csv


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

class EtlView(TemplateView):
    template_name = 'etl.html'

class ExcelCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'carga.html')

    def post(self, request, *args, **kwargs):
        ref = request.FILES['path']
        nom = str(ref)
        nombre = nom.split(".")
        usuario = User.objects.get(username = request.user.username)
        archivo = Archivo()
        archivo.usuario = usuario
        archivo.nombre = str(nombre[0])
        archivo.save()
        doc = Archivo.objects.get(id=archivo.id)
        file = csv.reader(request.FILES['path'], delimiter=',')
        for row in file:
            form = Excel()
            form.user = usuario
            form.archivo =doc
            form.producto = row[0]
            form.cliente = row[1]
            form.tipocliente = row[2]
            form.pais = row[3]
            form.ciudad = row[4]
            form.zona = row[5]
            form.estado = row[6]
            form.puntoventa = row[7]
            form.tipoproducto = row[8]
            form.fecha = row[9]
            form.ano = row[10]
            form.mesnumero = row[11]
            form.mes = row[12]
            form.dia = row[13]
            form.semestre = row[14]
            form.trimestre = row[15]
            form.semana = row[16]
            form.diasemana = row[17]
            form.empleado = row[18]
            form.cargo = row[19]
            form.cantidadventas = row[20]
            form.cantidadproductos = row[21]
            form.valorventa = row[22]
            form.save()
        return HttpResponseRedirect('/analisis/archivos/')

class ArchivoView(ListView):
    model = Archivo
    template_name = 'lista.html'
    context_object_name = 'archivos'
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Archivo.objects.all()
        else:
            queryset = Archivo.objects.filter(usuario=self.request.user.id)
        return queryset

class UsuariosList(ListView):
    model = User
    template_name = 'usuarios.html'
    context_object_name = 'usuarios'
    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=False)
        return queryset

class TodoView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'todo.html')

    def post(self, request, *args, **kwargs):
        print request.POST
        if request.POST['archivo']:
            archivo = request.POST['archivo']
            Datos = Excel.objects.filter(archivo__nombre=archivo)
        else:
            Datos = Excel.objects.all()
        return render(request, 'lista-carga.html', {'datos': Datos, 'campos':request.POST})

class DetalleView(View):
    def get(self, request, *args, **kwargs):
        archivo = self.kwargs['archivo']
        usuario = self.kwargs['usuario']
        return render(request, 'todo.html', {'archivo':archivo, 'usuario':usuario})

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