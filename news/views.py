from django.shortcuts import render, get_object_or_404
from .models import NewsArticle

def news_list(request):
    articles = NewsArticle.objects.all()
    categories = NewsArticle.CATEGORY_CHOICES
    
    category_filter = request.GET.get('category')
    if category_filter:
        articles = articles.filter(category=category_filter)
        
    context = {
        'articles': articles,
        'categories': [cat[0] for cat in categories],
        'current_category': category_filter,
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    context = {
        'article': article,
    }
    return render(request, 'news/news_detail.html', context)
