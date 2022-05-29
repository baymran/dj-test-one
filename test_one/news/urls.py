
from news.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', get_categories, name='category')

]
