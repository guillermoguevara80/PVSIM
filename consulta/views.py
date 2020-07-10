from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from consulta.models import Consulta
from consulta.forms import ConsultaForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

class ConsultaResp(View):
    form_class = ConsultaForm
    template= 'consulta/contacto.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        params = {}
        params['form'] = form
        return render(request, self.template, params)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            mail = form.cleaned_data["mail"]
            descripcion = form.cleaned_data["descripcion"]
            """"""
            # ############MESAJE DIRIGIDO AL SITIO #####################
            subject = "Nueva consulta de " + nombre
            desde = mail
            destino = ["guillermo.guevara.80@gmail.com"]
            mensaje_html = """<h1> Consulta de: """ + nombre + """</h1>""" +"""</h2>""" + """<br/><h2>Mail :""" + mail + """</h2>"""+ """<hr/><p>"""+ descripcion + """</p>"""
            #send_mail(subject, mensaje, desde, destino, html_message=mensaje_html,fail_silently=False)
            # ############MESAJE DIRIGIDO AL USUARIO #####################
            subject2 = "Consulta enviada satisfactoriamente"
            desde2 = "guillermo.guevara.80@gmail.com"
            destino2 = [mail]
            mensaje_html2 = """ <h1> Tu mensaje ha sido enviado exitosamente</h1><h2>En breve nos estaremos comunicando</<h2> 
                            <p>Este es un mail automatico, no debe ser respondido. </p> """
            #send_mail(subject2, mensaje, desde2, destino2, html_message=mensaje_html2,fail_silently=False)
            com = Consulta(nombre=nombre, mail=mail, descripcion=descripcion)
            com.save()
            params = {}
            params['form'] = form
            return HttpResponseRedirect('/myapp')
        else:
            return HttpResponseRedirect("/consulta/consulta")

            