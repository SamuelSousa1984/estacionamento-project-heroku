from django.shortcuts import render, redirect


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
