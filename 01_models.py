# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Recurso(models.Model):
    id = models.AutoField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    tipo_laboratorio = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    tipo_recurso = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Recurso'


class Reserva(models.Model):
    data_hora_chegada = models.DateTimeField(blank=True, null=True)
    data_hora_saida = models.DateTimeField(blank=True, null=True)
    disciplina = models.CharField(max_length=255, blank=True, null=True)
    justificativa = models.CharField(max_length=255, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    curso = models.CharField(max_length=255, blank=True, null=True)
    nome_professor = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    primeira_aula = models.BooleanField(blank=True, null=True)
    segunda_aula = models.BooleanField(blank=True, null=True)
    confirmacao = models.BooleanField(blank=True, null=True)
    id_recurso = models.IntegerField(blank=True, null=True)
    situacao = models.CharField(max_length=255, blank=True, null=True)
	tipo_recurso = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reserva'
