from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import  Http404
from django.http import HttpResponse

#Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Apps
from .models import ProyectosDibujantes
from .serializers import ProyectoDibujanteSerializer

bd = [
    {
        'title': 'Mont Blanc',
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Mont Blanc',
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Mont Blanc',
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
]

# Create your views here.
def principal(request):
    return render(request, 'dibujantes/principal.html')


def busqueda_proyecto(request):
    return render(request, 'dibujantes/busqueda.html')

#@api_view(['GET'])
def buscar(request):
    #print(request.GET['busqueda'])
    #print(request.GET['parametro'])
    if 'parametro' in request.GET:
        print(request.GET['parametro'])
        busqueda= request.GET['busqueda']
        parametro = request.GET['parametro']

        dibujante_asignado=''
        cliente_asignado=''
        cotizacion_asignada=''
        descripcion=''

        if parametro == 'Dibujante':
            #dibujante_asignado = busqueda
            descripcion = busqueda
        elif parametro == 'Cliente':
            cliente_asignado = busqueda
        elif parametro == '# Cotizacion':
            cotizacion_asignada = busqueda
            
        #try:   
        busqueda = ProyectosDibujantes.objects.filter(dibujante__contains=dibujante_asignado, cliente_externo__contains= cliente_asignado,cotizacion__contains=cotizacion_asignada,descripcion_proyecto__contains= descripcion  )
        # print(busqueda)
            #get_object_or_404(ProyectosDibujantes, dibujante__contains=dibujante_asignado, cliente_externo__contains= cliente_asignado,cotizacion=cotizacion_asignada)
        #except:
        #    raise Http404("Solicitud no encontrada, verifique e intente nuevamente")
        # print('this')
    else:
        busqueda = ProyectosDibujantes.objects.all()
        # print('that')
    # print(busqueda)
    return render(request, 'dibujantes/dashboard.html', {'busqueda': busqueda})

def retorno_busqueda(request):
    return render(request, 'dibujantes/dashboard.html', {'bd': bd})

def crearObra(request):
    return render(request, 'dibujantes/form_obra.html')

@api_view(['POST'])
def creacion(request):
    serializer = ProyectoDibujanteSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    info =serializer.save()

    return Response(ProyectoDibujanteSerializer(info).data)