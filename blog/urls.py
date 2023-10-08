from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostListView.as_view(),name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create-post/', views.CreatePostView.as_view(),name='create-post'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

]
