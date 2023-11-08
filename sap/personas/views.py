from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from personas.models import Persona


# Create your views here.
def agregar_persona(request):
    pass

def ver_persona(request, id):
    persona = Persona.objects.get(pk=id)
    datos = {'persona':persona}
    print(persona)
    pagina = loader.get_template('personas/ver.html')
    return HttpResponse(pagina.render(datos, request))