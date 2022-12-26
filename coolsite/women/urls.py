from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('cats/<int:categoryId>/', categories), # http://127.0.0.1:8000/cats/2/
    re_path(r"^archive/(?P<year>\d{4})/", archive) # http://127.0.0.1:8000/archive/2022/
]

