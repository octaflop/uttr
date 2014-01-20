#encoding: utf-8
from django import forms

from ckeditor.widgets import CKEditorWidget

from blog.models import BlogPost


class ReplyForm(forms.ModelForm):
    """
    model for replying to topic posts
    """
    draft = forms.CharField(widget=CKEditorWidget())
    slug = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = BlogPost
        exclude = ('entry', 'publish_date', 'source', 'poll', 'author', 'is_poll',
            'mod_notes', 'status', 'post_type', 'thread', 'tags', 'parent_post')

    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['draft'].label = 'Reply'
        self.fields['slug'].label = ''
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class BlogForm(forms.ModelForm):
    """
    Model form for topic creation / edits
    Only for admins
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


class PMForm(forms.ModelForm):
    """
    Model form for blog creation / edits
    """
    draft = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        exclude = ('publish_date', 'source', 'poll', 'author', 'is_poll', 'entry', 'mod_notes', 'parent_post', 'post_type', 'status', 'tags')

    def __init__(self, *args, **kwargs):
        super(PMForm, self).__init__(*args, **kwargs)
        self.fields['draft'].label = 'Message'
        self.fields['slug'].label = ''
        self.fields['slug'].widget = forms.HiddenInput()

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
