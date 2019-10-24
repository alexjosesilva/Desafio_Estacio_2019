# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Laboratorio(models.Model):
    tipo_laboratorio = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    id_recurso = models.ForeignKey('Recurso', models.DO_NOTHING, db_column='id_recurso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Laboratorio'


class Projetor(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    id_recurso = models.ForeignKey('Recurso', models.DO_NOTHING, db_column='id_recurso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Projetor'


class Recurso(models.Model):

    class Meta:
        managed = False
        db_table = 'Recurso'
