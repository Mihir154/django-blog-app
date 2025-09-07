from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Blog, Category, Comment

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

def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status="published")
    comments = Comment.objects.filter(blog=blog).order_by("-created_at")
    comment_count = comments.count()

    if request.method == "POST":
        if request.user.is_authenticated:
            body = request.POST.get("comment")
            if body and body.strip():
                Comment.objects.create(
                    blog=blog,
                    user=request.user,
                    body=body.strip()
                )
                return redirect("blog-detail", slug=slug)
        else:
            return redirect("login")

    context = {
        "blog": blog,
        "comments": comments,
        "comment_count": comment_count,
    }
    return render(request, "blog_detail.html", context)

def blog_search(request):
    keyword = request.GET.get("keyword", "")
    blogs = Blog.objects.filter(status="published").filter(
        Q(title__icontains=keyword) |
        Q(description__icontains=keyword) |
        Q(body__icontains=keyword)
    ).order_by("-created_at")

    context = {
        "blogs": blogs,
        "search_keyword": keyword,
    }
    return render(request, "blog_search.html", context)