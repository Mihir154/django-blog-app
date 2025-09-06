from django.shortcuts import render, redirect
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

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

@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login')
def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'dashboard/add_categories.html', context)