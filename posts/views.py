from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
) 

from .models import Post

# Create your views here.

# def home(request):
#     posts = Post.objects.all().order_by('-created_on')
#     return render(request, 'home.html', {'posts': posts})

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post


class PostUpdateView(UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['title', 'subtitle', 'body']

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = '/posts/list/'