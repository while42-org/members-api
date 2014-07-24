# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Member.photo'
        db.delete_column(u'while42_member', 'photo')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Member.photo'
        raise RuntimeError("Cannot reverse this migration. 'Member.photo' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Member.photo'
        db.add_column(u'while42_member', 'photo',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)


    models = {
        u'while42.chapter': {
            'Meta': {'ordering': "['city']", 'object_name': 'Chapter'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'while42.member': {
            'Meta': {'object_name': 'Member'},
            'chapter': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['while42.Chapter']", 'symmetrical': 'False'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'graduation_year': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['while42.Photo']", 'symmetrical': 'False'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'while42.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['while42']