# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Levenshtein.levenshtein_value'
        db.delete_column(u'levenshtein_levenshtein', 'levenshtein_value')

        # Deleting field 'Levenshtein.levenshtein_radio_info'
        db.delete_column(u'levenshtein_levenshtein', 'levenshtein_radio_info')

        # Adding field 'Levenshtein.distance'
        db.add_column(u'levenshtein_levenshtein', 'distance',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Levenshtein.ratio'
        db.add_column(u'levenshtein_levenshtein', 'ratio',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Levenshtein.levenshtein_value'
        db.add_column(u'levenshtein_levenshtein', 'levenshtein_value',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Levenshtein.levenshtein_radio_info'
        db.add_column(u'levenshtein_levenshtein', 'levenshtein_radio_info',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Levenshtein.distance'
        db.delete_column(u'levenshtein_levenshtein', 'distance')

        # Deleting field 'Levenshtein.ratio'
        db.delete_column(u'levenshtein_levenshtein', 'ratio')


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