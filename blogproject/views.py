from django.shortcuts import render, redirect
from blog.models import Blog
from .forms import CustomUserCreationForm

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

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)