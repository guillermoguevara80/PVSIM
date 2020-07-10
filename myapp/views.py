from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from myapp.models import Simulacion
from myapp.forms import CargarSim
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.forecast import forecast
from myapp.irradiance import irradiance_summer_winter
from myapp.position import sun_position

import os
from django.conf import settings

def index(request):
    #contenido = { 'nombre_sitio': 'PV Forecast' }
    #para_minorista = { 'tipo_usuario' : 'minorista' , 'incremento' : '25'}
    #para_mayorista = { 'tipo_usuario' : 'mayorista' , 'incremento' : '10'}
    return render(request,'myapp/index.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

    
def app_forecast(request):
    
    if request.method == 'POST':
        form = CargarSim(request.POST, request.FILES)

        if form.is_valid():
            Latitud = form.cleaned_data['Latitud']
            Longitud = form.cleaned_data['Longitud']
                
            fig=forecast(Latitud, Longitud,tz='America/Argentina/Buenos_Aires')
            newdoc = Simulacion.objects.create(Latitud = Latitud, Longitud=Longitud,)                       
            file='forecast/fig'+str(newdoc.id)+'.png'
            fig.savefig('media/'+file,transparent=True)
            newdoc.ruta_imagen.name = file
            newdoc.save()
            simu={'type':'7 Days Forecast'}
            return render(request,'myapp/results.html',{'newdoc':newdoc, 'simu':simu})
    else:
        form = CargarSim()
        
    return render(request, 'myapp/app_forecast.html', {'form': form})

def app_irradiance_summer_winter(request):
    
    if request.method == 'POST':
        form = CargarSim(request.POST, request.FILES)

        if form.is_valid():
            Latitud = form.cleaned_data['Latitud']
            Longitud = form.cleaned_data['Longitud']
                
            fig=irradiance_summer_winter(Latitud, Longitud,tz='America/Argentina/Buenos_Aires')
            newdoc = Simulacion.objects.create(Latitud = Latitud, Longitud=Longitud,)                       
            file='irradiance_summer_winter/fig'+str(newdoc.id)+'.png'
            fig.savefig('media/'+file, transparent=True)
            newdoc.ruta_imagen.name = file
            newdoc.save()
            simu={'type':'Summer&Winter Irradiance'}
            return render(request,'myapp/results.html',{'newdoc':newdoc,'simu':simu})
    else:
        form = CargarSim()
        
    return render(request, 'myapp/app_forecast.html', {'form': form})
    

def app_sun_position(request):
    
    if request.method == 'POST':
        form = CargarSim(request.POST, request.FILES)

        if form.is_valid():
            Latitud = form.cleaned_data['Latitud']
            Longitud = form.cleaned_data['Longitud']
            
            fig=sun_position(Latitud, Longitud,tz='America/Argentina/Buenos_Aires')
            newdoc = Simulacion.objects.create(Latitud = Latitud, Longitud=Longitud,)                       
            file='sun_position/fig'+str(newdoc.id)+'.png'
            fig.savefig('media/'+file, transparent=True)
            newdoc.ruta_imagen.name = file
            newdoc.save()
            simu={'type':'Sun Path'}
            
            return render(request,'myapp/results.html',{'newdoc':newdoc,'simu':simu})
    else:
        form = CargarSim()
        
    return render(request, 'myapp/app_forecast.html', {'form': form})