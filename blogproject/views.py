from django.shortcuts import render
from blog.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True)
    context = {
        'categories': categories,
        'featured_blogs': featured_blogs
    }
    return render(request, 'home.html', context)