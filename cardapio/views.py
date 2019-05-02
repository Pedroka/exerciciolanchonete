from django.shortcuts import render
from .models import Lanches, Ingredientes


def cardapio_lanches(request):
    context = {
        'lanches':Lanches.objects.all()
    }
    return render(request,'cardapio/lanches.html',context)


def monte_o_seu_lanche(request):
    context = {
        'ingredientes': Ingredientes.objects.all()
    }

    return render(request,'cardapio/monteoseu.html',context)