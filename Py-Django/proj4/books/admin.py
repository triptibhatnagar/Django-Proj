from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.register(Book)
class bookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'published_date', 'isbn')
    search_fields = ('title', 'author')
    ordering = ('published_date')