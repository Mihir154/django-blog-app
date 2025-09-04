from django.shortcuts import render
from blog.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True, status='published')
    blogs = Blog.objects.filter(is_featured=False, status='published')
    context = {
        'categories': categories,
        'featured_blogs': featured_blogs,
        'blogs': blogs,
    }
    return render(request, 'home.html', context)