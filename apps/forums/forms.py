# encoding: utf-8
# forms.py

from django import forms

from ckeditor.widgets import CKEditorWidget

from forums.models import Reply, Topic

class TopicForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Topic

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ReplyForm(forms.ModelForm):
    draft = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Reply
        exclude = ('date_created',)

    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['draft'].label = 'Reply'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
