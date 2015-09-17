from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse, FileResponse, HttpResponseRedirect

from . import forms

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

class MinhaView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Olá get')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Olá post')

class UploadView(View):

    def get(self, request, *args, **kwargs):
        form = forms.UploadFileForm()
        return render(request, 'upload.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload_arquivo( form.cleaned_data['arquivo'] )
            processando_latex( form.cleaned_data['arquivo'].name )
            return HttpResponseRedirect('/nucleo/')
        return render(request, 'upload.html', {'form': form})

# Imports para o upload de arquivos
import os
from django.conf import settings

def upload_arquivo(arquivo):
    with open(os.path.join(settings.UPLOAD_DIRECTORY, arquivo.name), 'wb') as destination:
        for chunk in arquivo.chunks():
            destination.write(chunk)

## Fazendo o processamento do latex
import subprocess, sys, tempfile

PADRAO_SUCESSO = b'Output written on'
ARQUIVO_VAZIO = b"*(Please type a command or say `\\end')"
ENTER_KEY = b'\n\r'

def processando_latex(path_arquivo):
    atual = os.getcwd()
    os.chdir('uploads')
    #os.chdir( tempfile.gettempdir() )#Entrar no diretorio temporario
    chamada = "pdflatex"
    #Verificando o SO
    if sys.platform.startswith('win'):
        chamada += '.exe'
    r = subprocess.Popen([chamada, path_arquivo], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    okay = False
    for line in r.stdout:
        if line == '' and r.poll() != None:
            r.stdin.write(ENTER_KEY)
            r.stdin.flush()
            r.communicate()
            break
        linha = line.rstrip()
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
