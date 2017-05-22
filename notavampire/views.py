from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic.base import TemplateView

def page_not_found(request):
        response = render(request, '404.html', {})
        response.status_code = 404
        return response

def handler500(request):
        response = render(request, '500.html', {})
        response.status_code = 500
        return response

class IndexView(TemplateView):
        template_name = "notavampire/index.html"

class NavFetch(TemplateView):
        template_name = "notavampire/nav.html"

class DepFetch(TemplateView):
        template_name = "notvampire/loaddep.html"
