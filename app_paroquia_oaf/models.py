# coding=utf-8

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


VALOR = ((u'dez', '10'), (u'vinte', '20'), (u'trinta','30'), (u'cinquenta', '50'),(u'cem', '100'))
TIPO = ((u'Mensal','Mensal'),(u'Sazonal', 'Sazonal'))

class pessoa(models.Model):
    '''
        Esta classe guarda o nome endereco e o tipo de regularidade em pagamentos do contribuinte, que estao nos valores
        ate R$ 100,00.
    '''

    nome = models.CharField(max_length=150)
    logradouro = models.CharField(max_length=150)
    numero_residencial = models.CharField(max_length=100)
    valor_de_carne = models.CharField(choices=VALOR, max_length=3,)
    tipo_de_regularidade = models.CharField(max_length=8)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pessoa"

class pessoa_valor_branco(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    logradouro = models.CharField(max_length=150)
    valor = models.FloatField()
    numero_residencial = models.CharField(max_length=100)
    tipo_de_regularidade = models.CharField(max_length=8)

    #usuario = models.ForeignKey(User)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Pessoa valores em Braco"
        db_table = "valores em branco"

class receita_ate_50(models.Model):
    '''
        Esta classe tem o objetivo de cadastrar os valores pagos pelos contribuintes
    '''
    responsavel_pelo_recebimento = models.CharField(max_length=100, unique_for_month=True)
    valor_recebido = models.IntegerField()
    pessoa_contribuinte = models.ForeignKey(pessoa)
    mes_referente = models.DateField(default=datetime.now(), blank=True)


    def __unicode__(self):
        return self.responsavel_pelo_recebimento

    class Meta:
        verbose_name_plural = "Receita ate 50"


class receita_maior_50(models.Model):
    responsavel_pelo_recebimento = models.CharField(max_length=100)
    valor_recebido = models.IntegerField()
    pessoa_contribuinte = models.ForeignKey(pessoa_valor_branco)
    mes_referente = models.DateField(default=datetime.now(), blank=True)


    def __unicode__(self):
        return self.responsavel_pelo_recebimento

    class Meta:
        verbose_name_plural = "Receita maior que 50"


class despesa(models.Model):
    responsavel_pela_despesa = models.CharField(max_length=100)
    valor_retirado = models.FloatField()
    data_retirada = models.DateField(default=datetime.now(), blank=True)
    #usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.responsavel_pela_despesa

    class Meta:
        verbose_name_plural = "Despesa"


class Emcaixa(models.Model):
    """
    Esta classe recebera a diferenca entre a receita e a despesa

    """
    valor = models.FloatField()
    data = models.DateField(default=datetime.now(), blank=True)



    def __unicode__(self):
        return self.valor

