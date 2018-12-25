from django.shortcuts import render, redirect
from .models import (Pessoa, Veiculo, MovRotativo,
    Mensalista, MovMensalista, MovRotativo
)
from .forms import (PessoaForm, VeiculoForm, RotativoForm, MensalistaForm,
    MovMensalistaForm,
)


#Configurando minhas views
def home(request):
    context = {'mensagem': 'Olá mundo!'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def add_pessoas(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def add_veiculos(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculos.html', data)

    
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


def mov_rotat(request):
    mov_rotat = MovRotativo.objects.all()
    form = RotativoForm()
    data = {'mov_rotat': mov_rotat, 'form': form}
    return render(request, 'core/mov_rotat.html', data)


def add_rotativo(request):
    form = RotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mov_rotat')


def update_rotativo(request, id):
    data = {}
    movrotat = MovRotativo.objects.get(id=id)
    form = RotativoForm(request.POST or None, instance=movrotat)
    data['movrotat'] = movrotat
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_mov_rotat')
    else:
        return render(request, 'core/movrot_update.html', data)


def delete_rotat(request, id):
    rotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        rotativo.delete()
        return redirect('core_mov_rotat')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': rotativo})


def mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/mensalistas.html', data)


def add_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mensalistas')


def update_mensal(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('core_mensalistas')
    else:
        return render(request, 'core/update_mensal.html', data)


def delete_mensal(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})


def mov_mensal(request):
    mensal = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mensal': mensal, 'form': form}
    return render(request, 'core/mov_mensal.html', data)


def add_movmensal(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mov_mensal')


def update_movmensal(request, id):
    data = {}
    movmensal = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensal)
    data['movmensal'] = movmensal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_mov_mensal')
    else:
        return render(request, 'core/update_movmensal.html', data)


def delete_movmensal(request, id):
    movmensal = MovMensalista.objects, get(id=id)
    if request.method =='POST':
        movmensal.delete()
        return redirect('core_mov_mensal')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movmensal})
