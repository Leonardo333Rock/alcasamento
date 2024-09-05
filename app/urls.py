from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('lista_de_presentes',views.Lista_de_presentes, name='lista_de_presentes'),
    path('confirmacao',views.Confimacao, name='confirmacao'),
    path('noivos',views.Noivos, name='noivos'),
    path('cerimonia',views.Cerimonia, name='cerimonia'),
    path('local',views.Local, name='Local'),
    path('add',views.Add, name='add'),
    path('add_convidado',views.Add_convidado, name='add_convidado'),
    path('acompanhantes',views.Acompanhantes,name='acompanhantes'),
    path('lista_de_convidados',views.Lista_de_convidados,name="lista_de_convidados"),
    path('editar/<int:id>',views.Edit_convidado,name='edit_convidado'),
    path('edit',views.Edit,name='edit'),
    path('lista_adm',views.Lista_adm,name='lista_adm'),
    path('editar_presente/<int:id>',views.Editar_presente,name='editar_presente'),
    path('editar_p',views.Editar_p,name='editar_p'),
    path('adm',views.Adm,name='adm'),
    path('confirmado',views.Confirmado,name='confirmado'),
    path('presentear/<int:id>',views.Presentear,name='presentear'),
    path('presente_escolhido',views.Presente_escolhido,name='presente_escolhido'),
    path('agradecimeto',views.Agradecimeto,name='agradecimeto'),
    path('pagina_de_cadastro',views.Pagina_de_cadastro,name='pagina_de_cadastro'),
    path('login',views.Login,name='login')








]