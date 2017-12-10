# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Contact, Page

admin.site.register(Contact)

admin.site.register(Page)