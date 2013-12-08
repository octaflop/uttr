# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table(u'blog_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'blog', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table(u'blog_blogpost')


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blog']