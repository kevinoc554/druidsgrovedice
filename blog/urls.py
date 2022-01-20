from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogposts, name='blog'),
    path('post/<int:blog_id>/', views.blog_post, name='blog_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:blog_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:blog_id>/', views.delete_post, name='delete_post'),
]
