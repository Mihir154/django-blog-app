from django.shortcuts import render
from blog.models import Blog

# def home(request):
#     blogs = Blog.objects.filter(status="published").order_by("-created_at")
#     featured_blogs = blogs.filter(is_featured=True)[:5]

#     context = {
#         "blogs": blogs,
#         "featured_blogs": featured_blogs,
#     }
#     return render(request, "home.html", context)

def home(request):
    blogs = Blog.objects.filter(status="published").order_by("-created_at")
    featured_blogs = blogs.filter(is_featured=True)[:5]
    recent_blogs = blogs.exclude(id__in=featured_blogs.values_list("id", flat=True))[:10]

    context = {
        "featured_blogs": featured_blogs,
        "recent_blogs": recent_blogs,
    }
    return render(request, "home.html", context)