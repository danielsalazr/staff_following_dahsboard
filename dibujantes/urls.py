from django.urls import path
from .views import (
    principal,
    busqueda_proyecto,
    retorno_busqueda,
    crearObra,
    buscar,
    creacion,
)

urlPathName = 'dibujantes/'

urlpatterns = [
    path(urlPathName, principal, name= 'principal'),
    path(urlPathName+'busqueda/', busqueda_proyecto, name= 'busqueda'),
    path(urlPathName+'buscar/', buscar, name= 'buscar'),
    path(urlPathName+'dashboard/', retorno_busqueda, name= 'dashboard'),
    path(urlPathName+'crear/', crearObra, name= 'crear'),
    path(urlPathName+'creacion/', creacion, name= 'creacion'),
]

