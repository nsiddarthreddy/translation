# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Levenshtein.levenshtein_ratio'
        db.add_column(u'levenshtein_levenshtein', 'levenshtein_ratio',
                      self.gf('django.db.models.fields.FloatField')
                             (null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Levenshtein.levenshtein_ratio'
        db.delete_column(u'levenshtein_levenshtein', 'levenshtein_ratio')

    models = {
        u'levenshtein.levenshtein': {
            'Meta': {'object_name': 'Levenshtein'},
            'created': ('django.db.models.fields.DateTimeField', [],
                        {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'levenshtein_ratio': ('django.db.models.fields.FloatField', [],
                                  {'null': 'True', 'blank': 'True'}),
            'levenshtein_value': ('django.db.models.fields.IntegerField', [],
                                  {'null': 'True', 'blank': 'True'}),
            'text_1': ('django.db.models.fields.TextField', [], {}),
            'text_2': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['levenshtein']
