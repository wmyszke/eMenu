# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Danie(models.Model):
    nazwa = models.CharField(max_length=150,blank=False, null=False, unique=True)
    zdjecie = models.ImageField(upload_to = 'zdjecia/')
    def __unicode__(self):
        return self.nazwa

class Menu(models.Model):
    nazwa = models.CharField(max_length=150,blank=False, null=False, unique=True)
    zdjecie = models.ImageField(upload_to = 'zdjecia/')
    nalezenie = models.ManyToManyField(Danie, through='NalezyDo')
    def __unicode__(self):
        return self.nazwa

class NalezyDo(models.Model):
    danie = models.ForeignKey(Danie)
    menu = models.ForeignKey(Menu)
    class Meta:
        unique_together = ('danie', 'menu')
    def __unicode__(self):
        d = self.danie
        m = self.menu
        w = str(m) + ' - ' + str(d)
        return w.decode('utf-8')
    
class Blad(models.Model):
    tresc = models.TextField()
    email = models.CharField(max_length=30, null=True)