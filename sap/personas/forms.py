from django.forms import ModelForm, EmailInput

from personas.models import Persona


class PersonaFormulario(ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'sexo', 'email', 'activo','curso')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }