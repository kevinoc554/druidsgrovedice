from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import BlogPost
from .forms import BlogForm


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
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to do that.')
        return redirect('home')
    if request.method == 'POST':
        data = {
            'author': request.user,
            'title': request.POST['title'],
            'content': request.POST['content']
        }
        form = BlogForm(data, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post successfully added.')
            return redirect(reverse('blog_post', args=[post.id]))
    form = BlogForm()
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_post(request, blog_id):
    """
    A view to edit and update the content of a blog post
    """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to do that.')
        return redirect('home')
    post = get_object_or_404(BlogPost, pk=blog_id)
    form = BlogForm(instance=post)
    template = 'blog/edit_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
