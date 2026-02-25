from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
) 

urlpatterns = [
#    path('posts/', views.home, name='home'),
   path('list/', PostListView.as_view(), name='post_list'),
   path('new/', PostCreateView.as_view(), name='post_new'),

   path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
   path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
