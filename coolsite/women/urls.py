from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'), # http://127.0.0.1:8000/
    path('about/', About.as_view(), name='about'), # http://127.0.0.1:8000/about
    path('addpage/', AddPage.as_view(), name='add_page'), # http://127.0.0.1:8000/add_page
    path('contact/', contact, name='contact'), # http://127.0.0.1:8000/contact
    path('login/', login, name='login'), # http://127.0.0.1:8000/login
    path('page/<slug:post_slug>/', ShowPost.as_view(), name='post'), # http://127.0.0.1:8000/post
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'), # http://127.0.0.1:8000/post
]
