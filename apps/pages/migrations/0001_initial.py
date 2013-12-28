# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Announcement'
        db.create_table(u'pages_announcement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'pages', ['Announcement'])

        # Adding model 'File'
        db.create_table(u'pages_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uttr_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'pages', ['File'])


    def backwards(self, orm):
        # Deleting model 'Announcement'
        db.delete_table(u'pages_announcement')

        # Deleting model 'File'
        db.delete_table(u'pages_file')


    models = {
        u'pages.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'entry': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pages.file': {
            'Meta': {'object_name': 'File'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uttr_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['pages']