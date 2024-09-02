from django.db import models

class Presente(models.Model):
    id = models.AutoField(primary_key=True)
    presente =  models.TextField(max_length=255)
    valor = models.FloatField()
    descricao = models.TextField(max_length=350, default='')
    link_img = models.TextField(max_length=255, default='')
    quantidades = models.IntegerField(default=0)


class Convidado(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    acompanhantes = models.IntegerField()
    codigo = models.IntegerField()
    confirmaçao = models.TextField(max_length=25, default='aberto')


    class Meta:
        ordering = ['acompanhantes']


class Convidados_confirmados(models.Model):
    id = models.AutoField(primary_key=True)
    db_convidados = models.TextField(max_length=255)


class Presentes_ganho(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    codigo = models.IntegerField()
    id_presente = models.IntegerField(default=0)
    nome_presente = models.TextField(max_length=255, default='')




