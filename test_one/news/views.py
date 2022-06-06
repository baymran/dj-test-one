from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import News, Category
from django.http import HttpResponse
from .forms import NewsForm
# Create your views here.
def index(request):
    news = News.objects.all()
    response = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', response)
    # t = loader.get_template('news/index.html', 'news/read_more.html')
    #
    # return HttpResponse(t.render(response, request))

def get_categories(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'news/category.html', context)

def read_more(request,  news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'news/read_more.html', context)

def post_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            print(news)
            return redirect(news)
    else:
        form = NewsForm()
    context = {'form': form}
    print(form.errors.as_data())
    return render(request, 'news/post_news.html', context)