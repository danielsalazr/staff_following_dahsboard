from django.contrib import admin
from .models import ProyectosDibujantes

# Register your models here.

@admin.register(ProyectosDibujantes)
class ProyectosDibujantes(admin.ModelAdmin):
    list_display= (
        'consecutivo_planos',
        'cotizacion',
        'cliente_externo',
        'dibujante',
    )