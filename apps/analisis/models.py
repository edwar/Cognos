# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Archivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = "Archivos"

    def __str__(self):
        return self.nombre

class Excel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    producto = models.CharField(max_length=50, null=True, blank=True)
    cliente = models.CharField(max_length=50, null=True, blank=True)
    tipocliente = models.CharField(max_length=15, null=True, blank=True)
    pais = models.CharField(max_length=15, null=True, blank=True)
    ciudad = models.CharField(max_length=15, null=True, blank=True)
    zona = models.CharField(max_length=15, null=True, blank=True)
    estado = models.CharField(max_length=10, null=True, blank=True)
    puntoventa = models.CharField(max_length=15, null=True, blank=True)
    tipoproducto = models.CharField(max_length=15, null=True, blank=True)
    fecha = models.CharField(max_length=15, null=True, blank=True)
    ano = models.CharField(max_length=4, null=True, blank=True)
    mesnumero = models.CharField(max_length=2, null=True, blank=True)
    mes = models.CharField(max_length=15, null=True, blank=True)
    dia = models.CharField(max_length=15, null=True, blank=True)
    semestre = models.CharField(max_length=10, null=True, blank=True)
    trimestre = models.CharField(max_length=10, null=True, blank=True)
    semana = models.CharField(max_length=10, null=True, blank=True)
    diasemana = models.CharField(max_length=10, null=True, blank=True)
    empleado = models.CharField(max_length=20, null=True, blank=True)
    cargo = models.CharField(max_length=20, null=True, blank=True)
    cantidadventas = models.CharField(max_length=10, null=True, blank=True)
    cantidadproductos = models.CharField(max_length=10, null=True, blank=True)
    valorventa = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Dato'
        verbose_name_plural = "Datos"

    def __str__(self):
        return self.producto