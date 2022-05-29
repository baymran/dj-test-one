from django.shortcuts import render
from .models import News, Category
from django.http import HttpResponse
# Create your views here.
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    response = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }
    return render(request, 'news/index.html', response)

def get_categories(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
        'categories': categories
    }
    return render(request, 'news/category.html', context)