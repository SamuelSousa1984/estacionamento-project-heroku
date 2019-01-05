from django.urls import path, re_path, include
from .views import index, contato, sobre, servico, planos, sistema


urlpatterns = [
    path('', index, name='website_home'),
    path('contato', contato, name='website_contato'),
    path('planos', planos, name='website_planos'),
    path('sobre', sobre, name='website_sobre'),
    path('servico', servico, name='website_servico'),
    path('sistema', sistema, name='website_sistema'),
]
