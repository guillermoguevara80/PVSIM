from django.forms import ModelForm
from .models import Simulacion

class CargarSim(ModelForm):
    class Meta:
        model=Simulacion
        fields=['Latitud','Longitud']
        error_messages={'Latitud':{'required':('Se debe agregar la Latituda')},
                        'Longitud':{'required':('Se debe agregar la longitud')},
        
                        
                        }
    def __init__(self,*args,**kwargs):
        super(CargarSim,self).__init__(*args,**kwargs)
        


