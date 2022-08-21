from django.db import models

# Create your models here.
class ProyectosDibujantes(models.Model):
    consecutivo_planos = models.CharField(max_length=30)
    cotizacion = models.IntegerField(default=0)
    version = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()
    prioridad = models.CharField(max_length=15)
    dibujante = models.CharField(max_length=60)
    cliente_interno = models.CharField(max_length=50)
    cliente_externo = models.CharField(max_length=50)
    zona_venta = models.CharField(max_length=60)
    descripcion_proyecto = models.TextField(max_length=600)
    grado_complejidad = models.CharField(max_length=60)
    visita_campo = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)
    fecha_salida = models.DateField(max_length=60)
