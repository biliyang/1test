# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django import forms
from .models import position, NewUser, Comment, Author, Article, Image
# Register your models here.


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_name', 'company_name', 'city', 'salary', 'education', 'workyear', 'createTime', 'postedweb')


class NewUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'profile')


class CommentAdamin(admin.ModelAdmin):
    list_display = ('user_id','article_id','pub_date','content','poll_num')


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(
        attrs={'rows': 41,
               'cols': 100}
    )},
    }
    list_display = ('title', 'pub_date', 'poll_num',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'article_id')


admin.site.register(position, PositionAdmin)
admin.site.register(NewUser, NewUserAdmin)
admin.site.register(Comment, CommentAdamin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Image, ImageAdmin)
