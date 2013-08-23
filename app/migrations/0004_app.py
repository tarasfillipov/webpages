# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'app_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'app', ['Book'])

        # Adding M2M table for field notes on 'Book'
        m2m_table_name = db.shorten_name(u'app_book_notes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'app.book'], null=False)),
            ('note', models.ForeignKey(orm[u'app.note'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'note_id'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'app_book')

        # Removing M2M table for field notes on 'Book'
        db.delete_table(db.shorten_name(u'app_book_notes'))


    models = {
        u'app.book': {
            'Meta': {'object_name': 'Book'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Note']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'app.note': {
            'Meta': {'object_name': 'Note'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['app']