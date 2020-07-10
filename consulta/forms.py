from django.forms import ModelForm
from consulta.models import Consulta

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre', 'mail', 'descripcion']
        error_messages = {
        'nombre': {'required': ("Se debe agregar un nombre de producto"),},
        'mail': {'required': ("Se debe agregar un email valido"),},
        'descripcion': {'required': ("Recordar cargar el mensaje")},
                        }
    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
    