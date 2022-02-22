from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import PC_DATA


def index(request):
    ordered = PC_DATA.objects.order_by('id')[:3]
    template = loader.get_template('monitor/index.html')
    context = {
        'ordered': ordered,
    }
    output = ', '.join([str(q.packages_l_h) for q in ordered]).__str__()
    return HttpResponse(template.render(context, request))


def overview(request):
    ordered = PC_DATA.objects.order_by('id')[:3]
    template = loader.get_template('monitor/overview.html')
    context = {
        'ordered': ordered,
    }
    output = ', '.join([str(q.packages_l_h) for q in ordered]).__str__()
    return HttpResponse(template.render(context, request))
