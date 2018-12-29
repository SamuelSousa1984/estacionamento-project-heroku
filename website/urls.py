from django.urls import path, re_path, include
from .views import index

urlpatterns = [
    path('', index, name='website_home')
]
