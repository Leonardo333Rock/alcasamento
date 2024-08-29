from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Presente, Convidado
import random
from . ultilizar import Sortear

def Home(request):
    return render(request,'home.html')

def Lista_de_presentes(request):
    presente = Presente.objects.all()
    for x in presente:
        print(x.valor)
    return render(request,'lista_de_presentes.html',{'presente':presente})

def Confimacao(request):
    if request.method == 'GET':
        return render(request, 'confirmacao.html')
    convite = str(request.POST.get('convite'))

    try:
        convidado = Convidado.objects.get(codigo=convite)
        
        repeticoes = [i for i in range(convidado.acompanhantes)]
        return render(request, 'acompanhantes.html',{'convidado':repeticoes,'conv':convidado.nome})
    except:
        return HttpResponse("<h1>Convinte nao Existe!</h1>")



def Confirmado(request):
    if request.method == 'POST':
        return HttpResponse('confirmado')
def Acompanhantes(request):
    return HttpResponse('OLA')

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

def Add_convidado(request):
    if request.method == 'GET':
        return render(request, 'add_convidado.html')
    else:
        
        convidado = Convidado()
        codigo = Convidado.objects.all()
        convidado.nome = request.POST.get("nome")
        convidado.acompanhantes = int(request.POST.get("qt_acompanhante"))

        numero  = Sortear(codigo)

        convidado.codigo = numero
        convidado.save()
        return redirect('add_convidado')


def Lista_de_convidados(request):
    convidado = Convidado.objects.all()
    quantidade = len(convidado)
    ac = 0
    for x in convidado:
        ac += x.acompanhantes

    total = quantidade + ac
    return render(request, 'lista_de_convidados.html',{'convidado':convidado,'quantidade':quantidade ,"ac":ac , 'total':total})


def Edit_convidado(request,id):
    if request.method == 'GET':
        convi = Convidado.objects.get(id=id)
        return render(request, 'edit_convidado.html',{'convidado':convi})

def Edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            convidado = Convidado.objects.get(id=id)
            convidado.nome = request.POST.get("nome")
            convidado.acompanhantes = int(request.POST.get("qt_acompanhante"))
            convidado.save()
            return redirect('lista_de_convidados')


def Lista_adm(request):
    presente = Presente.objects.all()
    return render(request,'lista_de_presentes_adm.html',{'presente':presente})


def Editar_presente(request,id):
    presente = Presente.objects.get(id=id)
    return render(request,'editar_presente.html',{'presente':presente})

def Editar_p(request):
        if request.method == "POST":
            id = request.POST.get("id")
            presente = Presente.objects.get(id=id)
            presente.presente = request.POST.get("presente")
            presente.quantidades = request.POST.get('quantidade')
            presente.descricao = request.POST.get("descricao").upper()
            presente.save()
            return redirect('lista_de_presentes')


def Adm(request):
    return render(request,'adm.html')