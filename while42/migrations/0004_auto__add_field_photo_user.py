# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field photos on 'Member'
        db.delete_table(db.shorten_name(u'while42_member_photos'))

        # Adding field 'Photo.user'
        db.add_column(u'while42_photo', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['while42.Member']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding M2M table for field photos on 'Member'
        m2m_table_name = db.shorten_name(u'while42_member_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'while42.member'], null=False)),
            ('photo', models.ForeignKey(orm[u'while42.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'photo_id'])

        # Deleting field 'Photo.user'
        db.delete_column(u'while42_photo', 'user_id')


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
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'while42.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['while42.Member']"})
        }
    }

    complete_apps = ['while42']
