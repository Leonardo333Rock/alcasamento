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

    class Meta:
        ordering = ['acompanhantes']