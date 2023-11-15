from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from personas.forms import PersonaFormulario
from personas.models import Persona


# Create your views here.

# PersonaFormulario = modelform_factory(Persona, exclude=['activo',])
def agregar_persona(request):
    pagina = loader.get_template('personas/agregar.html')
    if request.method == 'GET':
        formulario = PersonaFormulario
    elif request.method == 'POST':
        formulario = PersonaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario':formulario}
    return HttpResponse(pagina.render(datos,request))

def modificar_persona(request, id):
    pagina = loader.get_template('personas/modificar.html')
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'GET':
        formulario = PersonaFormulario(instance=persona)
    elif request.method == 'POST':
        formulario = PersonaFormulario(request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_persona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    datos = {'persona':persona}
    # print(persona)
    pagina = loader.get_template('personas/ver.html')
    return HttpResponse(pagina.render(datos, request))

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
        return redirect('inicio')
