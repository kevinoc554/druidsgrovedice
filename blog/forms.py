from django import forms
from .models import BlogPost, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('author', 'title', 'content', 'image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ""
