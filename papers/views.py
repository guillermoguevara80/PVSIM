from django.shortcuts import render

# Create your views here.

from papers.models import Papers
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from papers.forms import SearchPaperForm
import json
from django.http import HttpResponse

from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext




class BuscarPaper(View):
    def get(self, request):
        if request.is_ajax:
            palabra = request.GET.get('term', '')
            print(palabra)
            paper = Papers.objects.filter(titulo__icontains=palabra)
            results = []
            for an in paper:
                data = {}
                data['label'] = an.titulo
                results.append(data)
            data_json = json.dumps(results)
        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)


class BuscarPaper2(View):
    def get(self, request):
        if request.is_ajax:
            q = request.GET['valor']
            paper = Papers.objects.filter(titulo__icontains=q)
            results = []
            for rec in paper:
                print(rec.titulo)
                #print(rec.fecha)
                print(rec.ruta_imagen)

                data = {}
                data['titulo'] = rec.titulo
                
                data['contenido'] = str(rec.contenido)
                results.append(data)
            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)



def index(request):
    params = {}
    search = SearchPaperForm()
    params['search'] = search
    return render(request, 'papers/index.html', params)


class Index(View):
    model = Papers
    template = 'papers/index.html'

    def get(self, request):

        params = {}
        papers = Papers.objects.all().order_by('fecha')

        paginator = Paginator(papers, 3)
        page = request.GET.get('page')
        try:
            papers1 = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            papers1 = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            papers1 = paginator.page(paginator.num_pages)
        params['papers1'] = papers1
        search = SearchPaperForm()
        params['search'] = search
        return render(request, self.template, params)



class Paper(View):
    template = 'papers/paper.html'

    def get(self, request, slug):

        params = {}
        paper = Papers.objects.get(slug=slug)
        params['paper'] = paper

        return render(request, self.template, params)
