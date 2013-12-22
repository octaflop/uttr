#encoding: utf-8
from django import forms

from blog.models import BlogPost

class BlogForm(forms.ModelForm):
    """
    Model form for blog creation / edits
    """
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['entry'].label = 'Blog Post'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = BlogPost
        exclude = ('publish_date', 'source', 'poll', 'author',)

