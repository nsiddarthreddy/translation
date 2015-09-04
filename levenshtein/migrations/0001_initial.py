# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Levenshtein'
        db.create_table(u'levenshtein_levenshtein', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_1', self.gf('django.db.models.fields.TextField')()),
            ('text_2', self.gf('django.db.models.fields.TextField')()),
            ('distance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'levenshtein', ['Levenshtein'])


    def backwards(self, orm):
        # Deleting model 'Levenshtein'
        db.delete_table(u'levenshtein_levenshtein')


    models = {
        u'levenshtein.levenshtein': {
            'Meta': {'object_name': 'Levenshtein'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'text_1': ('django.db.models.fields.TextField', [], {}),
            'text_2': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['levenshtein']