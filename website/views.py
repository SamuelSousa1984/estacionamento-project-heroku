from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core import templates


def index(request):
    return render(request, 'FrontEndFiles/index.html')


def contato(request):
    return render(request, 'FrontEndFiles/contatos.html')


def planos(request):
    return render(request, 'FrontEndFiles/planos.html')


def sobre(request):
    return render(request, 'FrontEndFiles/sobre.html')


def servico(request):
    return render(request, 'FrontEndFiles/serviços.html')


@login_required
def sistema(request):
    return render(request, 'core/index.html')
