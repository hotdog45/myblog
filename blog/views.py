# -*- coding: utf-8 -*-
from django.shortcuts import render
# from django.http import HttpResponse
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})

