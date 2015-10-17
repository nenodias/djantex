# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AlunoTrabalho',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('arquivo', models.FileField(upload_to='')),
                ('data_entrega', models.DateField(null=True, blank=True)),
                ('nome_arquivo', models.TextField(blank=True)),
                ('aluno', models.ForeignKey(to='rest_api.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('nome_abreviado', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ano', models.IntegerField()),
                ('curso', models.ForeignKey(to='rest_api.Curso')),
                ('disciplina', models.ForeignKey(to='rest_api.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('data_criacao', models.DateField(null=True, blank=True)),
                ('data_entrega', models.DateField(null=True, blank=True)),
                ('professor', models.ForeignKey(to='rest_api.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='professor',
            name='usuario',
            field=models.ForeignKey(to='rest_api.Usuario'),
        ),
        migrations.AddField(
            model_name='alunotrabalho',
            name='trabalho',
            field=models.ForeignKey(to='rest_api.Trabalho'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(to='rest_api.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='usuario',
            field=models.ForeignKey(to='rest_api.Usuario'),
        ),
    ]
