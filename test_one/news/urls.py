
from news.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', get_categories, name='category'),
    path('news/<int:news_id>', read_more, name='read_more'),
    path('news/post_news', post_news, name='post_news')
]
