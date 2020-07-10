from django.db import models
import pytz
# Create your models here.
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Simulacion(models.Model):
    Latitud = models.FloatField('Latitude')
    Longitud = models.FloatField('Longitude')
    fecha_publicacion = models.DateTimeField('Date',default=timezone.now)    
    ruta_imagen = models.FileField(blank=True, null=True)
    
    
    