from django.urls import path
from django.urls import path
from consulta.views import ConsultaResp

urlpatterns = [
path('consulta',  ConsultaResp.as_view(), name='consultaresp'),
]
