# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse

def index(request):
    return render(request, "main/index.html")