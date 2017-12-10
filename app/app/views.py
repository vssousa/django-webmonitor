# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

def addUpdate(data, condition):
    if(condition == '1'):
        data['update'] = True
    return data

def index(request):
    data = {'content': 'home', 'active_home': True}
    return render(request, 'index.html', data)

def home(request, update):
    data = {'content': 'home', 'active_home': True}
    data = addUpdate(data, update)
    return render(request, 'index.html', data)

def contact(request, update):
    data = {'content': 'contact', 'active_contact': True}
    data = addUpdate(data, update)
    return render(request, 'contact.html', data)

def contactInfo(request, update, contact_id):
    data = {'content': 'contact', 'active_contact': True, 'contact_id': contact_id}
    data = addUpdate(data, update)
    return render(request, 'contact.html', data)

def about(request, update):
    data = {'content': 'about', 'active_about': True}
    data = addUpdate(data, update)
    return render(request, 'about.html', data)

def price(request, update):
    data = {'content': 'price', 'active_price': True}
    data = addUpdate(data, update)
    return render(request, 'price.html', data)