from dataclasses import fields
from rest_framework import serializers

from .models import ProyectosDibujantes

class ProyectoDibujanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectosDibujantes
        fields= '__all__'