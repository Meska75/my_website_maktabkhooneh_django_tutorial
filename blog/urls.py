from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path('', blog_view ,name='blog-index'),
    path('<str:pid>', blog_single,name='blog-single'),
    path('category/<str:cat_name>', blog_view,name='category'),
    path('author/<str:author_username>', blog_view,name='author'),
    path('tag/<str:tag_name>', blog_view,name='tag'),
    path('date/<str:date>', blog_view,name='date'),
    path('search/', blog_search,name='search'),
]