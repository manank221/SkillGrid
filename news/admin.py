from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date')
    list_filter = ('category', 'publication_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
