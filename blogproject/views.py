from django.shortcuts import render, redirect
from blog.models import Blog
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout

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
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            # user = form.get_user()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            auth_login(request, user)

            return redirect("home")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("home")