from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'), # http://127.0.0.1:8000/
    path('about/', About.as_view(), name='about'), # http://127.0.0.1:8000/about
    path('addpage/', AddPage.as_view(), name='add_page'), # http://127.0.0.1:8000/add_page
    path('contact/', contact, name='contact'), # http://127.0.0.1:8000/contact
    path('login/', LoginUser.as_view(), name='login'), # http://127.0.0.1:8000/login
    path('logout/', logout_user, name='logout'), # http://127.0.0.1:8000/login
    path('register/', RegisterUser.as_view(), name='register'), # http://127.0.0.1:8000/login
    path('page/<slug:post_slug>/', ShowPost.as_view(), name='post'), # http://127.0.0.1:8000/post
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'), # http://127.0.0.1:8000/post
]
