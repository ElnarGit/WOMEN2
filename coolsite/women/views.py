from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import *

menu = [{'title': 'О сайте','url_name': 'about'},
        {'title': 'Добавить статью','url_name': 'add_page'},
        {'title': 'Обратная связь','url_name': 'contact'},
        {'title': 'Войти','url_name': 'login'}
     ]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

#def index(request):
    #posts = Women.objects.all()

    #context = {
       # 'posts': posts,
        #'menu': menu,
        #'title': "Главная страница",
        #'cat_selected': 0,

   # }
    #return render(request,'women/index.html',context=context)

def about(request):
    data = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'women/about.html', context=data)

# def addpage(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     context = {
#         'form':form,
#         'menu': menu,
#         'title': 'Добавление статьи',
#         }
#     return render(request,'women/addpage.html',context=context)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context['title'] = "Добавление статьи"
        return context

def contact(request):
    return HttpResponseNotFound("Обратная связь")

def login(request):
    return HttpResponseNotFound("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DeleteView):
    model = Women
    template_name = 'women/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context['title'] = context['post']
        return context



# def show_post(request,post_id):
#     post = get_object_or_404(Women,pk=post_id)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#
#     }
#
#     return render(request,"women/post.html",context=context)




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

