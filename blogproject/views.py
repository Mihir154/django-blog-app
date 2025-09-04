from django.shortcuts import render
from blog.models import Blog, Category

def home(request):
    blogs = Blog.objects.filter(status="published").order_by("-created_at")
    featured_blogs = blogs.filter(is_featured=True)[:5]
    categories = Category.objects.all()

    context = {
        "blogs": blogs,
        "featured_blogs": featured_blogs,
        "categories": categories,
    }
    return render(request, "home.html", context)