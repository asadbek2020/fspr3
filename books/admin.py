from django.contrib import admin

from books.models import BookModel, AuthorModel, CategoryModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'page_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'author']


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
