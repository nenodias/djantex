from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    nome_abreviado = models.CharField(max_length=4)

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)

class Aluno(models.Model):
    '''Classe que representa os alunos'''
    usuario = models.ForeignKey(Usuario, blank=False, null=False)
    curso = models.ForeignKey(Curso, blank=False, null=False)
    ano = models.IntegerField()

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

class Professor(models.Model):
    usuario = models.ForeignKey(Usuario, blank=False, null=False)
    disciplina = models.ForeignKey(Disciplina, blank=False, null=False)
    curso = models.ForeignKey(Curso, blank=False, null=False)
    ano = models.IntegerField()

class Trabalho(models.Model):
    professor = models.ForeignKey(Professor)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)

class AlunoTrabalho(models.Model):
    aluno = models.ForeignKey(Aluno, blank=False, null=False)
    trabalho = models.ForeignKey(Trabalho, blank=False, null=False)
    arquivo = models.FileField()
    data_entrega = models.DateField(blank=True, null=True)
    nome_arquivo = models.TextField(blank=True)
