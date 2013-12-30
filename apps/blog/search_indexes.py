#encoding: utf-8

import datetime
from haystack import indexes
from blog.models import BlogPost

class BlogPostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publish_date = indexes.DateTimeField(model_attr='publish_date')

    def get_model(self):
        return BlogPost

    def index_queryset(self, using=None):
        now = datetime.datetime.now()
        return self.get_model().objects.filter(publish_date__lte=now)
