# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from menu.models import *
from django.http import HttpResponse
# szablony
from django.template import RequestContext, loader

# Create your views here.
def wyswietl_menu(request):
    m = Menu.objects.filter(nalezydo__menu__isnull=False).distinct().order_by('id') #-id descending
    #print(m)
    #print(m.values()[0]['id'])
    paginator = Paginator(m, 22)
    page = request.GET.get('page')
    try:
        menus = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        menus = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        menus = paginator.page(paginator.num_pages)
    a = ''
    template = loader.get_template('menu/menu.html')
    context = RequestContext(request, {
        'menus': menus,
    })
    return HttpResponse(template.render(context))

def wyswietl_po_nazwie(request):
    m = Menu.objects.filter(nalezydo__menu__isnull=False).distinct().order_by('nazwa')
    #print(m[0])
    paginator = Paginator(m, 22)
    page = request.GET.get('page')
    try:
        menus = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        menus = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        menus = paginator.page(paginator.num_pages)
    a = ''
    template = loader.get_template('menu/menus_wg_nazwy.html')
    context = RequestContext(request, {
        'menus': menus,
    })
    return HttpResponse(template.render(context))

def wyswietl_menu_po_ilosci_dan(request):
    from django.db.models import Count
    m = Menu.objects.filter(nalezydo__menu__isnull=False).values('nazwa').annotate(Count('nazwa')).order_by('-nazwa__count')
    #print(m[0]['nazwa'])
    paginator = Paginator(m, 22)
    page = request.GET.get('page')
    try:
        menus = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        menus = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        menus = paginator.page(paginator.num_pages)
    a = ''
    template = loader.get_template('menu/menu_wg_ilosci.html')
    context = RequestContext(request, {
        'menus': menus,
    })
    return HttpResponse(template.render(context))

def menu_details(request, menu_id):
    #menu = Menu.objects.filter(id=menu_id)
    #menu = Menu.objects.filter(id=menu_id,nalezydo__menu__isnull=False).distinct().order_by('id')
    menu_nazwa = Menu.objects.get(id=menu_id)
    #print(menu_nazwa)
    #print(menu.values()[0]['nazwa']) # Polskie
    #print(menu.values()[0]['id']) # 1
    dania = Danie.objects.filter(nalezydo__menu=menu_id)
    #print(d.values()[0]['nazwa'])
    #print(d[0].nazwa)
    
    for d in dania:
        tmp = str(d.zdjecie)
        if tmp[:8]=='zdjecia/':
            tmp = tmp[8:]
            d.zdjecie = tmp
            d.save()
        #d.save()
        #print(d.zdjecie)
    #print(dania[0].zdjecie)
    #quit()
    template = loader.get_template('menu/menu_detail.html')
    context = RequestContext(request, {
        'menu_nazwa': menu_nazwa,
        'dania':dania,
    })
    return HttpResponse(template.render(context))


def blad(request):
    return HttpResponse("Niezaimplementowany")


