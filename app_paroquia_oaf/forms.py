from django import forms
from models import *
from MetodosAdicionais import *


VALOR = ((u'10','10'),(u'20','20'),(u'50','50'))


class Formpessoa(forms.Form):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "style":"width:50%"}))
    logradouro = forms.CharField(max_length=150,widget=forms.TextInput(attrs={"class":"form-control", "style":"width:50%"}))
    numero_residencial = forms.IntegerField(label="Numero",widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))
    valor_cadastrado = forms.ChoiceField(choices=VALOR,widget=forms.Select(attrs={"class":"form-control", "style":"width:10%;"}))


class Formpessoa_valor_branco(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "style":"width:50%"}))
    valor = forms.IntegerField( widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%"}))
    logradouro = forms.CharField(max_length=150,widget=forms.TextInput(attrs={"class":"form-control", "style":"width:50%"}))
    numero_residencial = forms.IntegerField(label="Numero",widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))


    class Meta:
        model = pessoa_valor_branco
        fields = ['nome', 'valor','logradouro','numero_residencial']

class Formreceita_ate_50(forms.Form):
    responsavel_pelo_recebimento = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "style":"width:50%"}))
    valor_recebido = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))
    pessoa_contribuinte = forms.ModelChoiceField(queryset=pessoa.objects.all(),widget=forms.Select(attrs={"class":"form-control", "style":"width:50%"}))
    mes_referente = forms.DateField(widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))


class Formreceita_maior_50(forms.Form):
    responsavel_pelo_recebimento = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "style":"width:50%"}))
    valor_recebido = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))
    pessoa_contribuinte = forms.ModelChoiceField(queryset=pessoa_valor_branco.objects.all(),widget=forms.Select(attrs={"class":"form-control", "style":"width:50%"}))
    mes_referente = forms.DateField(widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))


class Formdespesas(forms.Form):

    responsavel_pela_despesa = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "style":"width:50%"}))
    valor_retirado = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))
    data_retirada = forms.DateField(widget=forms.TextInput(attrs={"class":"form-control", "style":"width:10%;"}))


class FormEmcaixa(forms.Form):

    valor = forms.FloatField(initial=soma(), label="Valor",widget=forms.TextInput(attrs={"class":"form-control", "style":"width:30%;"}))
    data = forms.DateField(label="Data", initial=datetime.date(datetime.now()),widget=forms.DateInput(format="%d/%m/%Y",attrs={"class":"form-control", "style":"width:40%;","readonly":"readonly"}))
    emcaixa = soma()