from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Presente, Convidado, Convidados_confirmados, Presentes_ganho
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User
from . ultilizar import Sortear, save_browser_os_info_to_file , get_browser_os_info


def Home(request):
    if request.method == "GET":
        return render(request,'home.html')

def Login(request):
    try:    
        if request.method == "GET":
            get_browser_os_info(request)
            return render(request,'login.html')
        else:
            cdv =  request.POST.get('cdv')
            senha =  '123'
            get_browser_os_info(request)


            user = authenticate(username=cdv, password=senha)
            if user:
                login(request, user)
                return render(request,'home.html')
            else:
                return HttpResponse('Convite incorreto')
    except:
            return render(request,'home.html')

@login_required(login_url='login')
def Lista_de_presentes(request):
    pg = Presentes_ganho.objects.all()
    presente = Presente.objects.all()
    return render(request,'lista_de_presentes.html',{'presente':presente, 'pg':pg})

@login_required(login_url='login')
def Presentear(request,id):
    presente = Presente.objects.get(id=id)
    return render(request, 'presentear.html',{'presente': presente})

@login_required(login_url='login')
def Presente_escolhido(request):
    try:
        nomero_do_convite = request.POST.get('nomero_do_convite')
        print(nomero_do_convite)
        convidado = Convidado.objects.get(codigo=int(nomero_do_convite))
        print(nomero_do_convite)
        id = request.POST.get('id')
        presente = Presente.objects.get(id=id)
        pg = Presentes_ganho()
        qt = presente.quantidades - 1

        pg.nome_presente = request.POST.get('presente')
        pg.nome = request.POST.get('nome')
        pg.codigo = nomero_do_convite
        pg.id_presente = id
        pg.save()

        presente.quantidades = qt
        presente.save()
        return redirect('agradecimeto')
    except:
        return HttpResponse("<h1>Convinte nao Existe!</h1>")
    
@login_required(login_url='login')
def Agradecimeto(request):
    return render(request, 'agradecimento.html')

@login_required(login_url='login')
def Confimacao(request):
    if request.method == 'GET':
        return render(request, 'confirmacao.html')
    convite = str(request.POST.get('convite'))

    try:
        convidado = Convidado.objects.get(codigo=convite)
        repeticoes = [i for i in range(convidado.acompanhantes)]
        if convidado.confirmaçao == 'aberto':
            return render(request, 'acompanhantes.html',{'convite':convite,'convidado':repeticoes,'conv':convidado.nome})
        else:
            return HttpResponse("<h1>Convinte Ja confirmado</h1>")

    except:
        return HttpResponse("<h1>Convinte nao Existe!</h1>")


@login_required(login_url='login')
def Confirmado(request):
    if request.method == 'POST':
        conv_confirmado = Convidados_confirmados()
        conv = request.POST.get('conv')
        convite = request.POST.get('convite')
        x = 0
        ac = conv
        while x < 3:
            ac0 = request.POST.get(str(x))
            if ac0 == None or ac0 == "":
                break
            ac += f'-{ac0}'
            x+=1
        
        conv_confirmado.db_convidados = ac
        conv_confirmado.save()
        convidado = Convidado.objects.get(codigo=convite)
        convidado.confirmaçao = 'fechado'
        convidado.save()
        return HttpResponse(f'confirmado')

@login_required(login_url='login')
def Acompanhantes(request):
    return HttpResponse('OLA')

@login_required(login_url='login')
def Noivos(request):
    return HttpResponse('noivos')


def Cerimonia(request):
    return HttpResponse('cerimonia')

def Local(request):
    return HttpResponse('local')



@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def Lista_de_convidados(request):
    convidado = Convidado.objects.all()
    quantidade = len(convidado)
    ac = 0
    for x in convidado:
        ac += x.acompanhantes

    total = quantidade + ac
    return render(request, 'lista_de_convidados.html',{'convidado':convidado,'quantidade':quantidade ,"ac":ac , 'total':total})

@login_required(login_url='login')
def Edit_convidado(request,id):
    if request.method == 'GET':
        convi = Convidado.objects.get(id=id)
        return render(request, 'edit_convidado.html',{'convidado':convi})
    
@login_required(login_url='login')
def Edit(request):
        if request.method == "POST":
            id = request.POST.get("id")
            convidado = Convidado.objects.get(id=id)
            convidado.nome = request.POST.get("nome")
            convidado.acompanhantes = int(request.POST.get("qt_acompanhante"))
            convidado.save()
            return redirect('lista_de_convidados')

@login_required(login_url='login')
def Lista_adm(request):
    presente = Presente.objects.all()
    return render(request,'lista_de_presentes_adm.html',{'presente':presente})

@login_required(login_url='login')
def Editar_presente(request,id):
    presente = Presente.objects.get(id=id)
    return render(request,'editar_presente.html',{'presente':presente})

@login_required(login_url='login')
def Editar_p(request):
        if request.method == "POST":
            id = request.POST.get("id")
            presente = Presente.objects.get(id=id)
            presente.presente = request.POST.get("presente")
            presente.quantidades = request.POST.get('quantidade')
            presente.descricao = request.POST.get("descricao").upper()
            presente.save()
            return redirect('lista_de_presentes')


@login_required(login_url='login')
def Adm(request):
    
    conf =  Convidados_confirmados.objects.all()

    for x in conf:
        arr = x.db_convidados.split("-")
    return render(request,'adm.html')


@login_required(login_url='login')
def Pagina_de_cadastro(request):
    if request.method == "GET":
        return render(request,'pg_de_casatro.html')
    else:
        cdv = request.POST.get('cdv')
        senha = '123'
        user = User.objects.create_user(username=cdv,password=senha)
        user.save()
        return render(request,'pg_de_casatro.html')


