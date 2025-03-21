from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

def imagem2(request):
    return render(request, 'galeria/imagem2.html')

def imagem3(request):
    return render(request, 'galeria/imagem3.html')

def imagem4(request):
    return render(request, 'galeria/imagem4.html')

def imagem5(request):
    return render(request, 'galeria/imagem5.html')

def imagem6(request):
    return render(request, 'galeria/imagem6.html')

def sobre(request):
    return render(request, 'galeria/sobre.html')