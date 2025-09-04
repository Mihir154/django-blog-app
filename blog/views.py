from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category

def category_posts(request, category_id):
    # category = get_object_or_404(Category, id=category_id)
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('home')

    blogs = Blog.objects.filter(category=category, status="published")
    categories = Category.objects.all()  # for navbar links

    context = {
        "blogs": blogs,
        "category": category,
        "categories": categories,
    }
    return render(request, "category_posts.html", context)
