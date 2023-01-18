"""projeto_codigos_DDD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from crud.views import home, lista_ddd, create_ddd, atualizar_ddd, deletar_ddd, sobre, listagem, consulta, busca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('listaddd/', lista_ddd, name="listaddd"),
    path('createddd/', create_ddd, name="createddd"),
    path('atualizarddd/<int:id_ddd>', atualizar_ddd, name= "url_atualizar_ddd"),
    path('deletarddd/<int:id_ddd>', deletar_ddd, name= "url_deletar_ddd"),
    path('sobre', sobre, name="sobre"),
    path('listagem/',listagem, name='listagem'),
    path('consulta/', consulta, name='consulta'), 
    path('busca/', busca, name='busca'),
    path('account/', include('django.contrib.auth.urls')),
]
