from django.contrib import admin
from .models import Category, Blog

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    ordering = ('name',)
    list_display_links = ('name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'status', 'is_featured', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_filter = ('status', 'is_featured', 'category', 'author')
    search_fields = ('title', 'author__username', 'category__name')
    ordering = ('-created_at',)
    list_editable = ('status', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin),
admin.site.register(Blog, BlogAdmin)