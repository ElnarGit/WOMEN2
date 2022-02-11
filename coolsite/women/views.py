from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
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
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,"Ошибка добавления поста")
    else:
        form = AddPostForm()
    context = {
        'form':form,
        'menu': menu,
        'title': 'Добавление статьи',
        }
    return render(request,'women/addpage.html',context=context)

def contact(request):
    return HttpResponseNotFound("Обратная связь")

def login(request):
    return HttpResponseNotFound("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request,post_id):
    post = get_object_or_404(Women,pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,

    }

    return render(request,"women/post.html",context=context)


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

