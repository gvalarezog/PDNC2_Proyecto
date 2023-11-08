from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from personas.models import Persona


# Create your views here.
def bienvenida(request):
    return HttpResponse ('Saludos')
def despedida(request):
    return HttpResponse ('<!DOCTYPE html>'
                         '<html><head></head><body><h1>Chao</h1></body>'
                         '</html>')


def mostrar_edad(request, edad):
    calculo_edad = 20 + edad
    return HttpResponse(f'Tu edad despues de 20 años será: {calculo_edad}')



def bienvenida2(request):
    cantidad_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('apellido', 'nombre')
    # print(f'Cantidad personas: {cantidad_personas}')
    dict_datos = {'cantidad_personas':cantidad_personas, 'personas':personas}
    pagina = loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos, request))





