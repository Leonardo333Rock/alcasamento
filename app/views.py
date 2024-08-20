from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Presente

def Home(request):
    return render(request,'home.html')

def Lista_de_presentes(request):
    presente = Presente.objects.all()
    for x in presente:
        print(x.valor)
    return render(request,'lista_de_presentes.html',{'presente':presente})

def Confimacao(request):
    return HttpResponse('confirmaçao')

def Noivos(request):
    return HttpResponse('noivos')

def Cerimonia(request):
    return HttpResponse('cerimonia')

def Local(request):
    return HttpResponse('local')

def Add(request):
    if request.method == 'GET':
        return render(request,'add_presente.html')
    else:
        id = Presente.objects.all()
        presente = Presente()
        presente.presente = request.POST.get("presente")
        presente.valor = int(request.POST.get("valor"))
        presente.quantidades = request.POST.get('quantidade')
        presente.descricao = request.POST.get("descricao").upper()
        presente.link_img = f"../../static/img/{presente.presente}{len(id)+1}.jpg"
        presente.save()
        return redirect('add')
