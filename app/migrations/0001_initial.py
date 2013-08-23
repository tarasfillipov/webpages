# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table(u'app_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'app', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table(u'app_note')


    models = {
        u'app.note': {
            'Meta': {'object_name': 'Note'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['app']