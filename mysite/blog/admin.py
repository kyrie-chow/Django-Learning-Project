from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'slug', 'publish', 'status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


# admin.site.register(Article, ArticleAdmin)
