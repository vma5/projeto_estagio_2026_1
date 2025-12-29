from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Admin padrão do Django
    path('', include('contato.urls')), # Nossas URLs customizadas
]