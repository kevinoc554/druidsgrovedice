from django.shortcuts import render
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
