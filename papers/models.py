from django.db import models

# Create your models here.

from ckeditor_uploader.fields import RichTextUploadingField

class Papers(models.Model):

    fecha = models.DateField(blank=True, null=True)
    contenido = RichTextUploadingField('contenido')
    slug = models.CharField(max_length=128, unique=True, default='---')
    ruta_imagen = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)
    titulo = models.CharField(max_length=200, default='---')
    resumen = models.CharField(max_length=200, default='---')