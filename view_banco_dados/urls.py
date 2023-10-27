"""
URL configuration for view_banco_dados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_discos, name='lista_discos'),
    path('disco/<int:disco_id>/', views.detalhes_disco, name='detalhes_disco'),
    path('cadastrar-disco/', views.cadastrar_disco, name='cadastrar_disco'),
    path('editar-disco/<int:disco_id>/', views.editar_disco, name='editar_disco'),
    path('excluir-disco/<int:disco_id>/', views.excluir_disco, name='excluir_disco'),
]
