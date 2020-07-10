from django.contrib import admin

# Register your models here.

from myapp.models import Simulacion


class SimulacionAdmin(admin.ModelAdmin):
    fields =['Latitud','Longitud' ,  'fecha_publicacion','ruta_imagen']
    list_display=['Latitud','Longitud' , 'fecha_publicacion','ruta_imagen']
    ordering = ['-fecha_publicacion']
    list_filter = ['fecha_publicacion']

admin.site.register(Simulacion, SimulacionAdmin)

