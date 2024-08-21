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



]