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
    tipo_de_regularidade = models.CharField(choices=TIPO,max_length=8)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pessoa"

class pessoa_valor_branco(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    logradouro = models.CharField(max_length=150)
    valor_de_carne = models.FloatField()
    numero_residencial = models.CharField(max_length=100)
    tipo_de_regularidade = models.CharField(choices=TIPO,max_length=8)

    #usuario = models.ForeignKey(User)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Pessoa valores em Braco"
        db_table = "valores em branco"

class receita_ate_50(models.Model):
    '''
        Esta classe tem o objetivo de cadastrar os valores pagos pelos contribuintes. Resume-se com valores ate R$ 100.
    '''
    hoje = datetime.today()
    responsavel_pelo_recebimento = models.CharField(max_length=100,)
    valor_recebido = models.FloatField()
    pessoa_contribuinte = models.ForeignKey(pessoa, unique_for_month=True)
    if hoje.month == 1:
        mes = 'janeiro'
    elif hoje.month ==2:
        mes = 'fevereiro'
    elif hoje.month == 3:
        mes = 'marco'
    elif hoje.month ==4:
        mes = 'abril'
    elif hoje.month ==5:
        mes = 'maio'
    elif hoje.month == 6:
        mes = 'junho'
    elif hoje.month == 7:
        mes = 'julho'
    elif hoje.month == 8:
        mes = 'agosto'
    elif hoje.month == 9:
        mes = 'setembro'
    elif hoje.month == 10:
        mes = 'outubro'
    elif hoje.month ==11:
        mes = 'novembro'
    elif hoje.month ==12:
        mes = 'dezembro'
    mes_referente = models.DateField(default=mes, blank=True)


    def __unicode__(self):
        return self.responsavel_pelo_recebimento

    class Meta:
        verbose_name_plural = "Receita ate R$ 100"


class receita_maior_50(models.Model):

    '''
        Esta classe tem o objetivo de cadastrar os valores pagos pelos contribuintes. Resume-se com valores acima de  R$ 100.
    '''

    hoje = datetime.today()
    responsavel_pelo_recebimento = models.CharField(max_length=100)
    valor_recebido = models.IntegerField()
    pessoa_contribuinte = models.ForeignKey(pessoa_valor_branco)
    if hoje.month == 1:
        mes = 'janeiro'
    elif hoje.month == 2:
        mes = 'fevereiro'
    elif hoje.month == 3:
        mes = 'marco'
    elif hoje.month ==4:
        mes = 'abril'
    elif hoje.month ==5:
        mes = 'maio'
    elif hoje.month == 6:
        mes = 'junho'
    elif hoje.month == 7:
        mes = 'julho'
    elif hoje.month == 8:
        mes = 'agosto'
    elif hoje.month == 9:
        mes = 'setembro'
    elif hoje.month == 10:
        mes = 'outubro'
    elif hoje.month ==11:
        mes = 'novembro'
    elif hoje.month ==12:
        mes = 'dezembro'
    mes_referente = models.DateField(default=mes, blank=True)


    def __unicode__(self):
        return self.responsavel_pelo_recebimento

    class Meta:
        verbose_name_plural = "Receita maior que R$ 100"


class despesa(models.Model):
    hoje = datetime.today()
    responsavel_pela_despesa = models.CharField(max_length=100)
    valor_retirado = models.FloatField()

    if hoje.month == 1:
        mes = 'janeiro'
    elif hoje.month ==2:
        mes = 'fevereiro'
    elif hoje.month == 3:
        mes = 'marco'
    elif hoje.month ==4:
        mes = 'abril'
    elif hoje.month ==5:
        mes = 'maio'
    elif hoje.month == 6:
        mes = 'junho'
    elif hoje.month == 7:
        mes = 'julho'
    elif hoje.month == 8:
        mes = 'agosto'
    elif hoje.month == 9:
        mes = 'setembro'
    elif hoje.month == 10:
        mes = 'outubro'
    elif hoje.month ==11:
        mes = 'novembro'
    elif hoje.month ==12:
        mes = 'dezembro'
    mes_referente = models.DateField(default=mes, blank=True)

    #usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.responsavel_pela_despesa

    class Meta:
        verbose_name_plural = "Despesa"


class Emcaixa(models.Model):
    """
    Esta classe recebera a diferenca entre a receita e a despesa

    """
    hoje = datetime.today()
    valor = models.FloatField()
    if hoje.month == 1:
        mes = 'janeiro'
    elif hoje.month ==2:
        mes = 'fevereiro'
    elif hoje.month == 3:
        mes = 'marco'
    elif hoje.month ==4:
        mes = 'abril'
    elif hoje.month ==5:
        mes = 'maio'
    elif hoje.month == 6:
        mes = 'junho'
    elif hoje.month == 7:
        mes = 'julho'
    elif hoje.month == 8:
        mes = 'agosto'
    elif hoje.month == 9:
        mes = 'setembro'
    elif hoje.month == 10:
        mes = 'outubro'
    elif hoje.month ==11:
        mes = 'novembro'
    elif hoje.month ==12:
        mes = 'dezembro'
    mes_referente = models.DateField(default=mes, blank=True)


    def __unicode__(self):
        return self.valor
