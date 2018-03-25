# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, CommentForm, SearchForm, CreateArticleForm
from .models import position, NewUser, Article, Comment, Poll, Author, Image, Keep
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from yzapp.lagoudetail import get_content, get_address, get_result
# Create your views here.
import urlparse, time, os, models

def index(request):
    latest_position_list = position.objects.all()
    paginator = Paginator(latest_position_list,15)

    try:
        # 得到request中的page参数
        pages = int(request.GET.get('page'))
    except:
        # 默认为1
        pages = 1
    if pages:
        latest_position_list = paginator.page(pages).object_list
    else:
        latest_position_list = paginator.page(1).object_list
    try:
        customer = paginator.page(pages)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    loginform = LoginForm()
    context = {'latest_position_list': latest_position_list,'loginform': loginform,'cus_list': customer}
    return render(request, 'index.html', context)

def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # url = request.POST.get('source_url','/yzapp')
                next = request.GET.get('next', '/')
                if request.GET.get('next') != '':
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponseRedirect('/yzapp/')
            else:
                return render(request, 'login.html', {'form': form,'错误': "用户名或密码错误!"})
        else:
            return render(request, 'login.html', {'form': form})


@login_required
def log_out(request):
    url = request.POST.get('source_url', '/yzapp/')
    logout(request)
    return redirect(url)

def register(request):
    error1 = "this name is already exist"
    valid = "this name is valid"

    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if request.POST.get('raw_username','erjgiqfv240hqp5668ej23foi') != 'erjgiqfv240hqp5668ej23foi':
            try:
                user = NewUser.objects.get(username=request.POST.get('raw_username'))
            except ObjectDoesNotExist:
               return render(request, 'register.html', {'form': form, 'msg': valid})
            else:
                return render(request,'register.html', {'form': form, 'msg': error1})
        else:
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return render(request, 'register.html', {'form': form, 'msg': "两个密码不相等,请从新输入"})
                else:
                    user = NewUser.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    author = Author.objects.create(name=username)
                    author.save()
                    return redirect('/yzapp/login')
            else:
                return render(request, 'register.html', {'form':form})


@login_required(login_url='/yzapp/login/')
def analysis(request, article_id):
    loginform = LoginForm()
    article = get_object_or_404(Article, id=article_id)
    image = Image.objects.filter(article=article_id)
    commentForm = CommentForm()
    comments = article.comment_set.all
    context = {'loginform': loginform, 'commentForm': commentForm, 'comments': comments, 'article': article, 'images': image}
    return render(request, 'anlysis.html',context)

@login_required(login_url='/yzapp/login/')
def item(request,position_id):
    latest_position=position.objects.get(id=position_id)
    content=get_content(position_id)
    address=get_address(content)
    result=get_result(content)
    loginform = LoginForm()
    return render(request, 'item.html', {'address': address,
                                         'result': result,
                                         'loginform': loginform,
                                         'latest_positon': latest_position})


def analysisBBS(request):
    loginform = LoginForm()
    latest_article_list = Article.objects.all()
    paginator = Paginator(latest_article_list, 10)

    try:
        # 得到request中的page参数
        pages = int(request.GET.get('page'))
    except:
        # 默认为1
        pages = 1
    if pages:
        latest_position_list = paginator.page(pages).object_list
    else:
        latest_position_list = paginator.page(1).object_list
    try:
        customer = paginator.page(pages)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    context = {'loginform': loginform,'latest_article_list': latest_article_list,'cus_list': customer}
    return render(request, 'analysisBBS.html', context)

@login_required(login_url='/yzapp/login/')
def comment(request, article_id):
    form = CommentForm(request.POST)
    url = urlparse.urljoin('/yzapp/analysisBBS/', article_id)
    if form.is_valid():
        user = request.user
        article = Article.objects.get(id=article_id)
        new_comment = form.cleaned_data['comment']
        c = Comment(content=new_comment, article_id=article_id)
        c.user = user
        c.save()
        article.comment_num += 1
        article.save()
    return redirect(url)


@login_required(login_url='/yzapp/login/')
def get_keep(request, article_id):
    logged_user = request.user
    article = Article.objects.get(id=article_id)
    keeps = logged_user.keep_set.all()
    articles = [];
    for keep in keeps:
        articles.append(keep.article)
    if article not in articles:
        article.user.add(logged_user)
        article.keep_num += 1
        article.save()
        keep = Keep(user=logged_user, article=article)
        keep.save()
        return redirect('/yzapp/analysisBBS/')
    else:
        article.keep_num -= 1
        article.save()
        Keep.objects.filter(article=article).delete()
        return redirect('/yzapp/analysisBBS/')


@login_required(login_url='/yzapp/login/')
def get_poll_article(request, article_id):
    logged_user = request.user
    article = Article.objects.get(id=article_id)
    polls = logged_user.poll_set.all()
    articles = [];
    for poll in polls:
        articles.append(poll.article)

    if article in articles:
        article.poll_num -= 1
        article.save()
        Poll.objects.filter(article=article).delete()
        return redirect('/yzapp/analysisBBS/')
    else:
        article.poll_num += 1
        article.save()
        poll = Poll(user=logged_user, article=article)
        poll.save()
        return redirect('/yzapp/analysisBBS/')



@csrf_protect
@login_required(login_url='/yzapp/login/')
def published(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            at = form.cleaned_data
            user = str(request.user)
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author=user,
            )
            article.save()
            image = Image.objects.create(
                name=form.cleaned_data['imagename'],
                img=form.cleaned_data['image'],
                article=article
            )
            image.save()
            return redirect('/yzapp/analysisBBS/')
    else:
        form = CreateArticleForm()
    return render(request, 'published.html', {'form': form})


@login_required(login_url='/yzapp/login/')
def postlist(request):

    user = str(request.user)
    article_list = Article.objects.filter(author=user)
    keep_list = Keep.objects.filter(user=request.user)
    return render(request, 'postlist.html',{'article_list': article_list, 'keep_list': keep_list})


def aricle_delete(request,article_id):
    Article.objects.filter(id=article_id).delete()
    return render(request, 'postlist.html')


def keeplist(request):
    user = request.user
    keep_list = Keep.objects.filter(user=user)
    return render(request, "keeplist.html", {'keep_list': keep_list})


def comment_delete(request, comment_id                                                                                                                                                           ):
    comment = Comment.objects.filter(id=comment_id).delete()
    return redirect('/yzapp/analysisBBS/')