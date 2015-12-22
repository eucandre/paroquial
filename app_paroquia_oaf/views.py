from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from forms import *


def apresentacao(request):
    return render_to_response("pagina_inicial.html")
@login_required()
def pessoas(request):
    if request.method=="POST":
        form = Formpessoa(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item = pessoa(nome = dados['nome'],logradouro = dados['logradouro'], numero_residencial=dados['numero_residencial'], valor_cadastrado=dados['valor_cadastrado'])
            item.save()
            return render_to_response("salvo.html", {})
    else:
        form = Formpessoa()
    return render_to_response("pessoa.html", {"form":form}, context_instance = RequestContext(request))

@login_required()
def pessoas_valor_em_branco(request):
    if request.method=='POST':
        form= Formpessoa_valor_branco(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("salvo.html", {})
    else:
        form = Formpessoa_valor_branco()
    return render_to_response("pessoa_valor_branco.html", {"form":form}, context_instance = RequestContext(request))

@login_required()
def receitas(request):
    if request.method=="POST":
        form = Formreceita_ate_50(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item = receita_ate_50(responsavel_pelo_recebimento = dados['responsavel_pelo_recebimento'],
                           valor_recebido = dados['valor_recebido'],
                           pessoa_contribuinte = dados['pessoa_contribuinte'],
                           mes_referente = dados['mes_referente'])
            item.save()
            return render_to_response("salvo.html", {})
    else:
        form = Formreceita_ate_50()
    return render_to_response("receita.html", {"form":form}, context_instance = RequestContext(request))


@login_required()
def receitass(request):
    if request.method=="POST":
        form = Formreceita_maior_50(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item = receita_maior_50(responsavel_pelo_recebimento = dados['responsavel_pelo_recebimento'],
                           valor_recebido = dados['valor_recebido'],
                           pessoa_contribuinte = dados['pessoa_contribuinte'],
                           mes_referente = dados['mes_referente'])
            item.save()
            return render_to_response("salvo.html", {})
    else:
        form = Formreceita_maior_50()
    return render_to_response("receita_mais50.html", {"form":form}, context_instance = RequestContext(request))


@login_required()
def despesas(request):
    if request.method == "post":
        form = Formdespesas(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item = despesa(responsavel_pela_despesa=dados['responsavel_pela_despesa'],valor_retirado=dados['valor_retirado'],
                           data_retirada=dados['data_retirada'])
            item.save()
            return render_to_response("salvo.html",{})
    else:
        form = Formdespesas()
    return render_to_response("despesas.html", {"form":form}, context_instance = RequestContext(request))

@login_required()
def valor_caixa(request):
    if request.method =='post':
        form = FormEmcaixa(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item = Emcaixa(valor = dados['valor'], data = dados['data'])
            item.save()
    else:
        form = FormEmcaixa()
    return render_to_response("emcaixa.html", {"form":form,"item":form.emcaixa, "itemd":form.data})

@login_required()
def lista_pessoas(request):
    global contribuintes_50, contribuintes_mais_50, lista_50, lista_mais_50
    try:

            itensp = len(pessoa.objects.all())
            itenspb = len(pessoa_valor_branco.objects.all())
            if itensp ==0 and itenspb==0:
                contribuintes_50 = "Sem registro"
                contribuintes_50 = "Sem registro"
                return render_to_response("lista_pessoas.html",)
            elif itensp > 0 and itenspb>0:
                contribuintes_50 = pessoa.objects.get(pk=itensp)
                contribuintes_mais_50 = pessoa_valor_branco.objects.get(pk=itenspb)
                lista_50 = pessoa.objects.all()
                lista_mais_50 = pessoa_valor_branco.objects.all()
                return render_to_response("lista_pessoas.html", {"itensp":itensp, "itemspb":itenspb, "pessoa_50":contribuintes_50, "pessoa_mais_50":contribuintes_mais_50, "lista_50":lista_50, "lista_mais_50":lista_mais_50 })
            elif itensp>0 and itenspb==0:
                contribuintes_50 = pessoa.objects.get(pk = itensp)
                lista_50 = pessoa.objects.all()
                return render_to_response("lista_pessoas.html", {"itensp":itensp, "itemspb":itenspb, "pessoa_50":contribuintes_50,"lista_50":lista_50})
            elif itensp==0 and itenspb>0:
                contribuintes_mais_50 = pessoa_valor_branco.objects.get(pk = itenspb)
                lista_mais_50 = pessoa_valor_branco.objects.all()
                return render_to_response("lista_pessoas.html",{"itensp":itensp, "itemspb":itenspb,"pessoa_mais_50":contribuintes_mais_50,"lista_mais_50":lista_mais_50 })
    except pessoa.DoesNotExist and pessoa_valor_branco.DoesNotExist:
        raise Http404()