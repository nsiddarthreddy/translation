# -*- coding: utf-8 -*-
from south.v2 import DataMigration
from levenshtein.utils import levenshte_ratio


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        levenshteins = orm.Levenshtein.objects.filter(levenshtein_ratio=None)
        for levenshtein in levenshteins:
            levenshtein.ratio_info = levenshte_ratio(levenshtein.text_1,
                                                     levenshtein.text_2)
            levenshtein.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'levenshtein.levenshtein': {
            'Meta': {'object_name': 'Levenshtein'},
            'created': ('django.db.models.fields.DateTimeField', [], {
                'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {
                'primary_key': 'True'}),
            'levenshtein_radio_info': ('django.db.models.fields.FloatField',
                                       [], {'null': 'True', 'blank': 'True'}),
            'levenshtein_value': ('django.db.models.fields.IntegerField',
                                  [], {'null': 'True', 'blank': 'True'}),
            'text_1': ('django.db.models.fields.TextField', [], {}),
            'text_2': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['levenshtein']
    symmetrical = True
