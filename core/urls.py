from django.urls import path, re_path, include
from .views import (home,
    lista_pessoas,
    add_pessoas,
    pessoa_update,
    pessoa_delete,
    lista_veiculos, 
    add_veiculos,
    veiculo_update,
    veiculo_delete,
    mov_rotat,
    add_rotativo,
    update_rotativo,
    delete_rotat,
    mensalista,
    add_mensalista,
    update_mensal,
    delete_mensal,
    mov_mensal,
    add_movmensal,
    update_movmensal,
    delete_movmensal,
    RelatorioCliente,
    RelatorioVeiculo,
    RelatorioMensalista,
    RelatorioMovRot,
    RelatorioMovMensal,
)

urlpatterns = [
    #Url index
    re_path('^$', home, name='core_home'),
    
    #Url dos clientes e cadastro de clientes
    re_path('^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path('^add_pessoas/$', add_pessoas, name='core_add_pessoas'),
    re_path('^pessoas_update/(?P<id>\d+)/$', pessoa_update, 
    name='core_pessoa_update'),
    re_path('^pessoas_delete/(?P<id>\d+)/$', pessoa_delete, 
    name='core_pessoa_delete'),
    
    #Url dos veículos e cadastro de veículos
    re_path('^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path('^add_veiculos$', add_veiculos, name='core_add_veiculos'),
    re_path('^update_veiculo/(?P<id>\d+)/$', veiculo_update, 
    name='core_veiculo_update'),
    re_path('^delete_veiculo/(?P<id>\d+)/$', veiculo_delete, 
    name='core_veiculo_delete'),

    #Url do movimento rotativo e de cadastro de movimento
    re_path('^movrotativo/$', mov_rotat, name='core_mov_rotat'),
    re_path('^addrotativo/$', add_rotativo, name='core_add_rotat'),
    re_path('^update-rotat/(?P<id>\d+)/$', update_rotativo, 
    name='core_update_rotativo'),
    re_path('^delete-rotat/(?P<id>\d+)/$', delete_rotat, 
    name = 'core_delete_rotativo'),
    
    #Url dos clientes mensalistas e de cadastro de mensalistas
    re_path('^mensalistas/$', mensalista, name='core_mensalistas'),
    re_path('^addmensalistas/$', add_mensalista, name='core_add_mensalista'),
    re_path('^updatemensal/(?P<id>\d+)/$', update_mensal, 
    name='core_update_mensal'),
    re_path('^delete_mensal/(?P<id>\d+)/$', delete_mensal, 
    name='core_delete_mensal'),
    
    #Url de movimento de mensalista e de cadastro dos mesmos
    re_path('^movmensal/$', mov_mensal, name='core_mov_mensal'),
    re_path('^addmovmensal/$', add_movmensal, name='core_add_movmensal'),
    re_path('^update_movmensal/(?P<id>\d+)/$', update_movmensal, 
    name='core_update_movmensal'),
    re_path('^delete_movmensal/(?P<id>\d+)/$', delete_movmensal, 
    name='core_delete_movmensal'),

    #Url do relatorio em PDF
    re_path('^relatorio-cliente/$', RelatorioCliente.as_view(), 
    name='relatorio_cliente'),
    re_path('^relatorio-veiculo/$', RelatorioVeiculo.as_view(), 
    name='relatorio_veiculo'),
    re_path('^relatorio-mensalista/$', RelatorioMensalista.as_view(), 
    name='relatorio_mensalista'),
    re_path('^relatorio-movrot/$', RelatorioMovRot.as_view(), 
    name='relatorio_movrot'),
    re_path('^relatorio-mov_mensal/$', RelatorioMovMensal.as_view(), 
    name='relatorio_movmensal'),
]
