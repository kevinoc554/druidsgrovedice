from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_on',
        'updated_on',
    )

    ordering = ('-created_on',)


admin.site.register(BlogPost, BlogPostAdmin)
