from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, categoryId):
    if request.GET:
        print("GEEEET", request.GET)
    if request.POST:
        print("POOOST", request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{categoryId}</p>")


def archive(request, year):
    if int(year) > 2023:
        raise Http404()
    if int(year) < 1900:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
