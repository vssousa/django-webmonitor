# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import ContactForm, PageForm
from django.views.decorators.csrf import csrf_exempt

from .models import Contact, Page


def index(request):
    contact_list = Contact.objects.order_by('name')
    return render(request, 'monitoring_board/contacts.html',
                  {'active_contacts': True, 'contact_list': contact_list})


def pages(request, contact_id):
    page_list = Page.objects.filter(contact=contact_id).order_by('-date')
    return render(request, 'monitoring_board/pages.html',
                  {'active_pages': True, 'page_list': page_list, 'contact_id': contact_id})


@csrf_exempt
def addContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            urls = form.cleaned_data.get('urls').split(',')
            dates = form.cleaned_data.get('dates').split(',')
            contacts = Contact.objects.filter(email=email)
            contact = None
            if contacts:
                contact = contacts[0]
            else:
                contact = Contact(email=email, name=name)
                contact.save()

            currentURL = None
            if len(urls) == len(dates):
                for i in range(len(urls)):
                    currentURL = urls[i]
                    newPage = Page(contact=contact, url=currentURL, date=dates[i])
                    newPage.save()

            return redirect(currentURL[:-2] + '/0/' + str(contact.id))
        else:
            return HttpResponse("Invalid contact form!")


@csrf_exempt
def addPage(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            contact_id = form.cleaned_data.get('contact_id')
            url = form.cleaned_data.get('url')
            date = form.cleaned_data.get('date')
            contact = get_object_or_404(Contact, pk=contact_id)
            newPage = Page(contact=contact, url=url, date=date)
            newPage.save()
            red = redirect(url[:-2] + "/0")
            print(red)
            return red
        else:
            return HttpResponse("Invalid page form!")
