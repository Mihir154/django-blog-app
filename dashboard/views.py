from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from blog.models import Category, Blog
from .forms import CategoryForm, PostForm


@login_required(login_url="login")
def dashboard(request):
    category_count = Category.objects.count()
    blog_count = Blog.objects.count()

    context = {
        "catcnt": category_count,
        "blogcnt": blog_count,
    }
    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="login")
def categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "dashboard/categories.html", context)


@login_required(login_url="login")
def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm()

    return render(request, "dashboard/add_categories.html", {"form": form})


@login_required(login_url="login")
def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm(instance=category)

    return render(request, "dashboard/edit_categories.html", {"form": form})


@login_required(login_url="login")
def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")


@login_required(login_url="login")
def posts(request):
    posts = Blog.objects.all()
    return render(request, "dashboard/posts.html", {"posts": posts})


@login_required(login_url="login")
def add_posts(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect("posts")
    else:
        form = PostForm()

    return render(request, "dashboard/add_posts.html", {"form": form})

@login_required(login_url='login')
def edit_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = request.user  # keep author as current user
            updated_post.slug = slugify(updated_post.title)  # update slug if title changes
            updated_post.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_posts.html', context)


@login_required(login_url="login")
def delete_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect("posts")