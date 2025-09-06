from django.shortcuts import render
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    categoryCount = Category.objects.all().count()
    blogCount = Blog.objects.all().count()

    context = {
        'catcnt': categoryCount,
        'blogcnt': blogCount
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')