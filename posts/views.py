from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView

) 

from .models import Post, Status
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     posts = Post.objects.all().order_by('-created_on')
#     return render(request, 'home.html', {'posts': posts})

class PostListView(ListView):
    template_name = 'posts/list.html'
    # model = Post
    published_status = Status.objects.get(name='published')
    # Queryset attribute allow us to select some data from the db by using the model class
    queryset = Post.objects.filter(status=published_status).order_by('-created_on').reverse()
    context_object_name = 'posts'



    # this method helps us use the context however we want (take a look at it, add elements or anything)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

# class PostListView(ListView):
#     template_name = 'posts/gallery.html'
#     published_status = Status.objects.get(name='published')
#     queryset = Post.objects.filter(status=published_status).order_by('-created_on').reverse()
#     context_object_name = 'posts'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#         return context


class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'status',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PostUpdateView(UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'status',]

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = '/posts/list/'

class PostDraftListView(ListView):
    template_name = 'posts/drafts.html'
    model = Post
    context_object_name = 'drafts'

    def get_queryset(self):
        draft_status = Status.objects.get(name='draft')
        return Post.objects.filter(status=draft_status).order_by('-created_on').reverse()

class PostArchivedListView(ListView):
    template_name = 'posts/archived.html'
    context_object_name = 'archived_posts'

    def get_queryset(self):
        archived_status = Status.objects.get(name='archived')
        return Post.objects.filter(status=archived_status).order_by('-created_on').reverse()