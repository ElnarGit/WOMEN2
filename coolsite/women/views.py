from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *

menu = [{'title': 'О сайте','url_name': 'about'},
        {'title': 'Добавить статью','url_name': 'add_page'},
        {'title': 'Обратная связь','url_name': 'contact'},
        {'title': 'Войти','url_name': 'login'}
     ]

def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': "Главная страница",
        'cat_selected': 0,

    }
    return render(request,'women/index.html',context=context)

def about(request):
    data = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'women/about.html', context=data)

def addpage(request):
    return HttpResponseNotFound("Добавление статьи")

def contact(request):
    return HttpResponseNotFound("Обратная связь")

def login(request):
    return HttpResponseNotFound("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request,post_id):
    return HttpResponseNotFound(f"Отоброжение статьи с id = {post_id}")

def show_category(request,cat_id):

    posts = Women.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': "Отображение по рубрикам",
        'cat_selected': 0,

    }
    return render(request, 'women/index.html', context=context)

