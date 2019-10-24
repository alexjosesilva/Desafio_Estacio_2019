from __future__ import unicode_literals
from django.contrib.auth.models import User
#https://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance.1.html
from django.contrib.auth.models import UserManager

from django.db import models
from django.template.defaultfilters import default


class Categoria(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    objetos = models.Manager()    
    def __str__(self):
        return  str(self.nome)  +" | "+ str(self.descricao)

class Curso(models.Model):
    nome=models.CharField(primary_key=True, max_length=255)
    objetos = models.Manager()    
    def __str__(self):
        return  str(self.nome) 
 
     

class Usuario(User):
    
   

    #user_ptr_id = models.CharField(primary_key=True, max_length=14, null=False, blank=False, default=1 )
    matricula = models.CharField(
    max_length=14,
    null=False,
    blank=False
    )
    
    nome = models.CharField(
    max_length=14,
    null=False,
    blank=False,
    default=""
    )

    #password =  models.CharField( max_length=8, null=False, blank=False )

    #email = models.CharField( max_length=255, null=False, blank=False )
    
    CATEGORIA = ( ('professor', 'professor'),
                    ('laboratorista', 'laboratorista'),
                    
                    )
    
    categoria = models.CharField(
                                     choices=CATEGORIA,
                                     default='professor', null=False,
    blank=False, max_length=255)
    
    timezone = models.CharField(max_length=50, default='America/Recife')
     
    objetos = UserManager()
    """
    class Meta:
        abstract =True
        """

    def __str__(self):
        return str(self.matricula)  + " | " +  str(self.nome)  + " | "+ str(self.email)
     
    
    
class Foo(models.Model):
    
    name = models.CharField(
    max_length=255,
    null=False,
    blank=False

    )

    objetos = models.Manager()
    
class TipoLaboratorio (models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    objetos = models.Manager()
    
    
    def __str__(self):
        return str(self.nome)  +" | "+ str(self.descricao) 
    
 
class Recurso(models.Model):
    LOCALIZACAO = ( ('terreo', 'terreo'),
                    ('1 andar', '1 andar'),
                    
                    )
    localizacao = models.CharField(choices=LOCALIZACAO,default='sem localizacao', null=True, blank=True, max_length=255)
    
    SALA = ( ('LAB 03', 'LAB 03'),
              ('LAB 04', 'LAB 04'),
              ('LAB 05', 'LAB 05'),
              ('LAB 06', 'LAB 06'),
              ('LAB 07', 'LAB 07'),
              ('LAB 08', 'LAB 08'),
              ('LAB 09', 'LAB 09'),
              ('LAB 10', 'LAB 10'),
              ('LAB 11', 'LAB 11'),
              ('LAB 13', 'LAB 13'),
              ('LAB 14', 'LAB 14'),
              ('LAB 15', 'LAB 15'),                    
              ('LAB 16', 'LAB 16'),
              ('LAB 17', 'LAB 17'),
              ('LAB 18', 'LAB 18'),
              ('LAB 19', 'LAB 19'),
              ('LAB 20', 'LAB 20'),
                    )
    sala = models.CharField(choices=SALA,default='LAB XX', null=True, blank=True, max_length=255)
   
    descricao = models.CharField(max_length=255, blank=True, null=True, default ="sem descricao")
    tipo_laboratorio = models.ForeignKey(TipoLaboratorio, on_delete=models.PROTECT, blank=True, null=True )#tem que ajustar para null?
    
    #Projetor
    numero = models.IntegerField(blank=True, null=True)
    
    tipo_recurso = models.CharField(max_length=255, blank=True, null=True)
    
    objetos = models.Manager()
    
    def __str__(self):
        if(self.tipo_recurso == "laboratorio"):
            return str(self.sala) +" | "+ str(self.tipo_laboratorio) + " | "+ str(self.localizacao) +" | " + str(self.descricao)
        else:
            return str(self.numero) + " | " + str(self.descricao)
    
 
class Situacao (models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    objetos = models.Manager()
    def __str__(self):
        return str(self.id) +" | "+ str(self.nome)  +" | "+ str(self.descricao) 
    

class Reserva(models.Model):
    data_hora_chegada = models.DateTimeField(blank=True, null=True)
    data_hora_saida = models.DateTimeField(blank=True, null=True)
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT)
    justificativa = models.CharField(max_length=255, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    confirmacao = models.BooleanField(blank=True, null=True)
    
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    id_recurso = models.ForeignKey(Recurso, on_delete=models.PROTECT) 
    tipo_recurso = models.CharField(max_length=255, blank=True, null=True)
    
    disciplina = models.CharField(max_length=255, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default = None,blank=True, null=True, )
    nome_professor = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    primeira_aula = models.BooleanField(blank=True, null=True)
    segunda_aula = models.BooleanField(blank=True, null=True) 
    
    objetos = models.Manager()
    
    def __str__(self):
        return str(self.id) +" | "+ str(self.data_hora_saida) + " | "+ str(self.data_hora_chegada) +" | " + str(self.situacao) +" | " + str(self.tipo_recurso)
