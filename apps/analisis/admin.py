from django.contrib import admin
from .models import Archivo, Excel

@admin.register(Archivo)
class ArchivooAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Excel)
class ExcelAdmin(admin.ModelAdmin):
    list_display = ('producto',)