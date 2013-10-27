# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tad'
        db.create_table(u'main_tad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('logged_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['Tad'])

        # Adding M2M table for field tags on 'Tad'
        m2m_table_name = db.shorten_name(u'main_tad_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tad', models.ForeignKey(orm[u'main.tad'], null=False)),
            ('tag', models.ForeignKey(orm[u'main.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tad_id', 'tag_id'])

        # Adding model 'Tag'
        db.create_table(u'main_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Tad'
        db.delete_table(u'main_tad')

        # Removing M2M table for field tags on 'Tad'
        db.delete_table(db.shorten_name(u'main_tad_tags'))

        # Deleting model 'Tag'
        db.delete_table(u'main_tag')


    models = {
        u'main.tad': {
            'Meta': {'object_name': 'Tad'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logged_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Tag']", 'symmetrical': 'False'})
        },
        u'main.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']