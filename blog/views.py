from django.shortcuts import render


def all_blogposts(request):
    """
    A view to return all blog posts,
    and render them on the Blog page
    """
    template = 'blog/blog.html'

    return render(request, template)
