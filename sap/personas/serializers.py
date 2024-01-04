from rest_framework import serializers

from personas.models import Persona, Curso


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('url','id','nombre', 'apellido', 'sexo', 'email', 'activo','curso',)

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('url','nombre', 'horas', 'profesor',)