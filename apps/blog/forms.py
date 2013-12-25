#encoding: utf-8
from django import forms

from ckeditor.widgets import CKEditorWidget

from blog.models import BlogPost


class BlogForm(forms.ModelForm):
    """
    Model form for blog creation / edits
    """
    entry = forms.CharField(widget=CKEditorWidget())
    draft = forms.CharField(widget=CKEditorWidget())
    mod_notes = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        exclude = ('publish_date', 'source', 'poll', 'author', 'is_poll')

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['entry'].label = 'Blog Post'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
