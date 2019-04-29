from django.contrib import admin
from .models import Article, Response, File, ArticleFile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(File)
class ResponseFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'email', 'created', 'updated')
    list_filter = ('created', 'email')
    search_fields = ('email', 'response')


@admin.register(ArticleFile)
class ResponseFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'created', 'updated', 'article')
    list_filter = ('file', 'created',)
    # search_fields = ('a',)

