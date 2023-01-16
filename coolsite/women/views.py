from django.contrib.auth import logout, login
from django.core.cache import cache
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        query = cache.get_or_set('women', Women.objects.filter(is_published=True).select_related('cat'), 60*3)
        # if not query:
        #     query = Women.objects.filter(is_published=True).select_related('cat')
        #     cache.set('women', query, 60*5)
        return query
        # return Women.objects.filter(is_published=True).select_related('cat')


class About(DataMixin, TemplateView):
    template_name = 'women/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О сайте')
        return context | c_def


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    # raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return context | c_def


def contact(request):
    return HttpResponse("Связаться с разработчиком")


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        title = context['post'].title
        c_def = self.get_user_context(title=title)
        return context | c_def


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        slug = self.kwargs['cat_slug']
        context = super().get_context_data(**kwargs)

        # c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c = cache.get(f'cat_{slug}')
        if not c:
            c = Category.objects.get(slug=slug)
            cache.set(f'cat_{slug}', c, 60)

        c_def = self.get_user_context(title='Категория - ' + c.name, cat_selected=c.pk)
        return context | c_def

    def get_queryset(self):
        query = cache.get_or_set('cat', Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat'), 60 * 3)
        # query = cache.get('cat')
        # if not query:
        #     query = Women.objects.filter(is_published=True).select_related('cat')
        #     cache.set('cat', query, 60 * 5)
        return query
        # return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
