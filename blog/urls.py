from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from django.contrib.auth.decorators import login_required
from blog import views as blog_views

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Apply login_required to class-based views
PostListView = method_decorator(login_required, name='dispatch')(PostListView)
PostDetailView = method_decorator(login_required, name='dispatch')(PostDetailView)
PostCreateView = method_decorator(login_required, name='dispatch')(PostCreateView)
PostUpdateView = method_decorator(login_required, name='dispatch')(PostUpdateView)
PostDeleteView = method_decorator(login_required, name='dispatch')(PostDeleteView)
UserPostListView = method_decorator(login_required, name='dispatch')(UserPostListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]