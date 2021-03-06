from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse, FileResponse, HttpResponseRedirect

from . import forms

class HomePageView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

class MinhaView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Olá get')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Olá post')

import tempfile
import pdb

class UploadView(View):

    def get(self, request, *args, **kwargs):
        form = forms.UploadFileForm()
        return render(request, 'upload.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                pasta_temporaria = tempfile.mkdtemp()
                upload_arquivo( form.cleaned_data['arquivo'], pasta_temporaria )
                nome_arquivo = form.cleaned_data['arquivo'].name
                extensao_arquivo = nome_arquivo[nome_arquivo.rfind('.'):]
                pdb.set_trace()
                if extensao_arquivo == '.tex':
                    pass
                elif extensao_arquivo == '.zip':
                    extrair_zip(nome_arquivo, pasta_temporaria)
                    nome_arquivo = nome_arquivo[:nome_arquivo.rfind('.')]
                    nome_arquivo += ".tex"
                else:
                    raise Exception('Arquivo não suportado')
                processando_latex( nome_arquivo, pasta_temporaria )
                arquivo_pdf = nome_arquivo[:nome_arquivo.rfind('.')] + '.pdf'

                arquivo_gerado = open(os.path.join(pasta_temporaria, arquivo_pdf), 'rb')
                response = HttpResponse(arquivo_gerado, content_type='application/pdf')
                #Para Baixar
                #response['Content-Disposition'] = 'attachment; filename="%s"'%(arquivo_pdf)
                #Para exibir
                response['Content-Disposition'] = 'inline; filename="%s"'%(arquivo_pdf)
                return response
            except Exception as ex:
                print(ex)
                return HttpResponse(ex, status=500)
        return render(request, 'upload.html', {'form': form})

# Imports para o upload de arquivos
import os
from django.conf import settings

def upload_arquivo(arquivo, pasta_temporaria):
    with open(os.path.join(pasta_temporaria, arquivo.name), 'wb') as destination:
        for chunk in arquivo.chunks():
            destination.write(chunk)

import zipfile

def extrair_zip(arquivo_zip, pasta_temporaria):
    atual = os.getcwd()
    os.chdir(pasta_temporaria)
    with zipfile.ZipFile(arquivo_zip, "r") as zipado:
        zipado.extractall(".")
    os.chdir(atual)

## Fazendo o processamento do latex
import subprocess, sys, tempfile

PADRAO_SUCESSO = b'Output written on'
ARQUIVO_VAZIO = b"*(Please type a command or say `\\end')"
PADRAO_NOME_ARQUIVO = b'**Please type the name of your input file.'
ENTER_KEY = b'\n\r'

def processando_latex(path_arquivo, pasta_temporaria):
    atual = os.getcwd()
    os.chdir(pasta_temporaria)
    chamada = 'pdflatex'
    #Verificando o SO
    if sys.platform.startswith('win'):
        chamada += '.exe'
    pdb.set_trace()
    r = subprocess.Popen([chamada, path_arquivo], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    okay = False
    for line in r.stdout:
        if line == '' and r.poll() != None:
            r.stdin.write(ENTER_KEY)
            r.stdin.flush()
            r.communicate()
            break
        linha = line.rstrip()
        if linha.find(PADRAO_NOME_ARQUIVO) != -1:
            texto_nome_bytes = str.encode(path_arquivo)
            r.stdin.write(texto_nome_bytes)
        if linha.find(PADRAO_SUCESSO) != -1:
            okay = True
        if linha.find(ARQUIVO_VAZIO) != -1:
            break
        print(linha)
        if r.stdin:
            r.stdin.write(ENTER_KEY)
            r.stdin.flush()
    print(okay)
    os.chdir(atual)
