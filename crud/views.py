from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import DDD
from .form import DDDForm

# Create your views here.
def home(request):
    return render(request, "layout.html")

def lista_ddd(request):
    ddds = DDD.objects.all()
    pacote = {"ddd_chave": ddds}
    return render(request, "listaddd.html", pacote)

def create_ddd(request):
    form = DDDForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listaddd")

    pacote = {"form_ddd": form}
    return render(request, "createddd.html", pacote)

def atualizar_ddd(request, id_ddd):
    ddd = DDD.objects.get(pk=id_ddd)
    
    form = DDDForm(request.POST or None, instance=ddd)
    if form.is_valid():
        form.save()
        return redirect("listaddd")

    pacote = {"form_ddd": form}
    return render(request, "createddd.html", pacote)

def deletar_ddd(request, id_ddd):
    ddd = DDD.objects.get(pk=id_ddd)
    ddd.delete()

    return redirect("listaddd")

def sobre(request):
    return render(request, "sobre.html")

def listagem(request):
 listatotal = DDD.objects.all()
 return render(request, 'listagem.html', {'listatotal':listatotal})

def consulta(request):
 return render(request, 'consulta.html')

def busca(request):
 buscar = request.GET.get('busca')
 resultados = DDD.objects.filter(ddd__icontains=buscar)
 return render(request, 'busca.html', {'resultados': resultados})
