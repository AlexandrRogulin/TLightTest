from django.shortcuts import render
from .models import Post
from django.db.models import Q


def index(request):
    search_query = request.GET.get("search", "")
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query) | Q(author__name__icontains=search_query))
    else:
        posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
