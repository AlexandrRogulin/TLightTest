from django.shortcuts import render
from django.http import HttpResponse
# Импортируем модель, чтобы обратиться к ней
from .models import Post, CustomUser
from django.views.generic import ListView
from django.db.models import Q

def index(request):
    search_query = request.GET.get("search", "")
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query) | Q(author__name__icontains=search_query))
    # elif search_query:
    #     posts = Post.objects.filter(author__icontain=search_query)
    else:
        posts = Post.objects.all()
        # posts = Post.objects.order_by('author')


    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
    


# class SearchResultsView(ListView):
#     model = Post
#     template_name = 'index.html'

#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         object_list = Post.objects.filter(
#             Q(title__icontains=query) | Q(body__icontains=query)
#         )
#         return object_list
