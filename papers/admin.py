from django.contrib import admin

# Register your models here.

from .models import Papers

class Papersadmin(admin.ModelAdmin):
    list_display = ['fecha', 'titulo']
    exclude = ['resumen', 'ruta_imagen']
    #def has_add_permission(self, request, obj=None):
    #    return False
    #def has_delete_permission(self, request, obj=None):
    #    return False

admin.site.register(Papers, Papersadmin)