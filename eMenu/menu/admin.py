# -*- coding: utf-8 -*-
from django.contrib import admin
from menu.models import Danie
from menu.models import Menu
from menu.models import NalezyDo

# Register your models here.
admin.site.register(Danie)
admin.site.register(Menu)
admin.site.register(NalezyDo)