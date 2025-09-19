from django.contrib import admin
from .models import Blog, BlogView


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'views_count')
    search_fields = ('title', 'content', 'author__username')




@admin.register(BlogView)
class BlogViewAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'viewed_at')
    list_filter = ('viewed_at',)