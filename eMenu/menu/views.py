# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from menu.models import *
from django.http import HttpResponse
# szablony
from django.template import RequestContext, loader

# Create your views here.
def wyswietl_menu(request):
    m = Menu.objects.filter(nalezydo__menu__isnull=False).order_by('id') #-id descending
    #print(m[0])
    a = ''
    template = loader.get_template('menu/menu.html')
    context = RequestContext(request, {
        'a': a,
    })
    return HttpResponse(template.render(context))

#wyswietl_menu(1)