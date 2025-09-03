from django.shortcuts import render
from blog.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home.html', context)