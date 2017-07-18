# -*- coding: utf-8 -*-

from django.contrib import admin

from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    

admin.site.register(Article,ArticleAdmin)