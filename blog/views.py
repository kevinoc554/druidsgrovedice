from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def all_blogposts(request):
    """
    A view to return all blog posts,
    and render them on the Blog page
    """
    first = BlogPost.objects.first()
    blogposts = BlogPost.objects.all()[1:]
    template = 'blog/blog.html'
    context = {
        'first': first,
        'blogposts': blogposts,
    }

    return render(request, template, context)


def blog_post(request, blog_id):
    """
    A view to return a specific blog post, and render it
    along with any comments.
    """
    post = get_object_or_404(BlogPost, pk=blog_id)
    print(post.created_on)
    print(post.updated_on)
    template = 'blog/blog_post.html'
    context = {
        'post': post,
    }

    return render(request, template, context)


def add_post(request):
    """
    A view to add a Blog Post
    """
    template = 'blog/add_post.html'
    context = {}

    return render(request, template, context)