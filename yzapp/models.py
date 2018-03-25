# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    profile = models.CharField('profile', default='', max_length=256)

    def __str__(self):
        return self.username


class Author(models.Model):
    name = models.CharField(max_length=256)
    register_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name


class position(models.Model):
    position_name = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)
    city = models.CharField(max_length=16)
    salary = models.CharField(max_length=16)
    education = models.CharField(max_length=16)
    workyear = models.CharField(max_length=16)
    createTime = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField('NewUser', blank=True)
    postedweb = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name = 'position'
        verbose_name_plural = 'position'


class Article(models.Model):
    title = models.CharField(max_length=256, null=True)
    author = models.CharField(max_length=256, null=True)
    user = models.ManyToManyField('NewUser', blank=True)
    content = models.TextField('content')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    published = models.BooleanField('published', default=False)
    poll_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    keep_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'


class Comment(models.Model):
    user = models.ForeignKey('NewUser', null=True)
    article = models.ForeignKey('Article', null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    poll_num = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Poll(models.Model):
    user = models.ForeignKey('NewUser', null=True)
    article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)


class Keep(models.Model):
    user = models.ForeignKey('NewUser', null=True)
    article = models.ForeignKey(Article, null=True)


class Image(models.Model):
    name = models.CharField(max_length=256)
    img = models.FileField(upload_to='')
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.name


class item_comment(models.Model):
    user = models.ForeignKey('NewUser', null=True)
    comment = models.ForeignKey('Comment')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    poll_num = models.IntegerField(default=0)
