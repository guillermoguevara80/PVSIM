from django.urls import path, include
from myapp import views
urlpatterns = [
 path('', views.index, name='index'),
 path('contacto', views.contacto, name='contacto'),
 path('app_forecast', views.app_forecast, name='app_forecast'),
 path('app_irradiance_summer_winter', views.app_irradiance_summer_winter, name='app_irradiance_summer_winter'),
 path('app_sun_position', views.app_sun_position, name='app_sun_position'),
 path('ckeditor/', include('ckeditor_uploader.urls')),
 ]