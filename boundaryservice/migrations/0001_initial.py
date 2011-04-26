# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BoundarySet'
        db.create_table('api_boundaryset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=256, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('singular', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('kind_first', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('authority', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('last_updated', self.gf('django.db.models.fields.DateField')()),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('metadata_fields', self.gf('boundaries.lib.fields.ListField')(separator='|', blank=True)),
        ))
        db.send_create_signal('api', ['BoundarySet'])

        # Adding model 'Boundary'
        db.create_table('api_boundary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=256, db_index=True)),
            ('set', self.gf('django.db.models.fields.related.ForeignKey')(related_name='boundaries', to=orm['api.BoundarySet'])),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('external_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=192, db_index=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('metadata', self.gf('boundaries.lib.fields.JSONField')(blank=True)),
            ('shape', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=4269)),
            ('simple_shape', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=4269)),
        ))
        db.send_create_signal('api', ['Boundary'])


    def backwards(self, orm):
        
        # Deleting model 'BoundarySet'
        db.delete_table('api_boundaryset')

        # Deleting model 'Boundary'
        db.delete_table('api_boundary')


    models = {
        'api.boundary': {
            'Meta': {'ordering': "('kind', 'display_name')", 'object_name': 'Boundary'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'metadata': ('boundaries.lib.fields.JSONField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '192', 'db_index': 'True'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boundaries'", 'to': "orm['api.BoundarySet']"}),
            'shape': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'simple_shape': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'db_index': 'True'})
        },
        'api.boundaryset': {
            'Meta': {'ordering': "('name',)", 'object_name': 'BoundarySet'},
            'authority': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_first': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateField', [], {}),
            'metadata_fields': ('boundaries.lib.fields.ListField', [], {'separator': "'|'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'singular': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'db_index': 'True'})
        }
    }

    complete_apps = ['api']
