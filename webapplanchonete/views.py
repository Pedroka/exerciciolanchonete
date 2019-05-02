from django.shortcuts import render
from cardapio.models import Lanches
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def falecosnosco(request):
    return render(request,'faleconosco.html')
