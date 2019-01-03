from django.urls import path, re_path, include
from .views import index, contato, sobre, servico, planos


urlpatterns = [
    path('', index, name='website_home'),
    path('', contato, name='website_contato'),
    path('', planos, name='website_planos'),
    path('', sobre, name='website_sobre'),
    path('', servico, name='website_servico'),
]
