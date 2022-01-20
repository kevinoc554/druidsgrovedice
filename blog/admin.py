from django.contrib import admin
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_on',
        'updated_on',
    )

    ordering = ('-created_on',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'post',
        'body',
        'created_on'
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
