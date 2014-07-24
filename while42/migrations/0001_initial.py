# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chapter'
        db.create_table(u'while42_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'while42', ['Chapter'])

        # Adding model 'Member'
        db.create_table(u'while42_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('work', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('graduation_year', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'while42', ['Member'])

        # Adding M2M table for field chapter on 'Member'
        m2m_table_name = db.shorten_name(u'while42_member_chapter')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'while42.member'], null=False)),
            ('chapter', models.ForeignKey(orm[u'while42.chapter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'chapter_id'])


    def backwards(self, orm):
        # Deleting model 'Chapter'
        db.delete_table(u'while42_chapter')

        # Deleting model 'Member'
        db.delete_table(u'while42_member')

        # Removing M2M table for field chapter on 'Member'
        db.delete_table(db.shorten_name(u'while42_member_chapter'))


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
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['while42']