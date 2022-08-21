from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def menuInicio(request):
    return render(request, 'inicio.html')