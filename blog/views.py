from django.shortcuts import render
from .models import *

# Create your views here.
def category_posts(request, category_id):
    blogs = Blog.objects.filter(category_id=category_id, status='published')
    context = {
        'blogs': blogs,
        'category_id': category_id
    }
    return render(request, 'category_posts.html', context)