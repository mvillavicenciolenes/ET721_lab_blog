from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # List all posts
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Detail of a post
    path('post/new/', views.post_create, name='post_create'),  # Create a new post
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),  # Edit an existing post
]