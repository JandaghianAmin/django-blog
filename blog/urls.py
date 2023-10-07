from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(),name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create-post/', views.CreatePostView.as_view(),name='create-post'),

]
