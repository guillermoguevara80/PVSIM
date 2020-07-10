from django.urls import path


from papers.views import Index, Paper, BuscarPaper, BuscarPaper2, index

urlpatterns = [
    #path('', index, name='index'),
    path('', Index.as_view(), name='papers'),
    path('papers/<slug:slug>/', Paper.as_view(), name='paper'),
    path('buscar_paper/', BuscarPaper.as_view(), name='buscar_paper'),
    path('buscar_paper2/', BuscarPaper2.as_view(), name='buscar_paper2'),
    ]