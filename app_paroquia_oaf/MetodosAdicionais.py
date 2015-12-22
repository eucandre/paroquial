# coding=utf-8
from django.http import Http404
from reportlab.lib import styles
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from models import *
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica
from datetime import *



def soma():
    global somada
    try:

        tamanhoR = len(receita_ate_50.objects.all())
        tamanhoRR = len(receita_maior_50.objects.all())
        tamanhoD = len(despesa.objects.all())
        if tamanhoR ==0 and tamanhoRR==0:
            return 0
        elif tamanhoR >0 and tamanhoRR >0 and tamanhoD==0:
            r = receita_ate_50.objects.get(pk=tamanhoR)
            rr = receita_maior_50.objects.get(pk=tamanhoRR)

            valor = int(r.valor_recebido)+int(rr.valor_recebido)
            return valor
        elif tamanhoR>0 and tamanhoRR==0 and tamanhoD==0:
            r = receita_ate_50.objects.get(pk = tamanhoR)
            raux = receita_ate_50.objects.get(pk = (tamanhoR-1))
            valor = int(r.valor_recebido)+int(raux.valor_recebido)
            return valor
    except receita_ate_50.DoesNotExist and receita_maior_50.DoesNotExist:
        raise Http404()


def Cria_Documento_pdf():
    tamanho50= len(receita_ate_50.objects.all())
    tamanho_50= len(receita_maior_50.objects.all())
    tamanhoP50 = len(pessoa.objects.all())
    tamanhoP_50 = len(pessoa_valor_branco.objects.all())
    if tamanho50==0 and tamanho_50==0 and tamanhoP50==0 and tamanhoP_50==0:
        c = Canvas("relatorio.pdf")

        c.drawString(50,800,"Relatorio para a Paroquia santo antonio")
        valor=0
        listmes = str(datetime.now())

        c.drawString(50,750,"Mes da receita")
        c.drawString(50,725,listmes[5]+listmes[6])
        c.drawString(150,750,"Valor da receita")
        c.drawString(150,725,str(valor))
        c.drawString(250, 750,"Contribuintes ate 50")
        c.drawString(250, 725,str(valor))
        c.drawString(400, 750,"Contribuintes acima de 50")
        c.drawString(400, 725,str(valor))
        c.save()
        c.showPage()
    elif tamanho50>0:
        r = receita_ate_50.objects.get(pk = tamanho50)
        p50 = pessoa.objects.get(pk=pessoa.objects.all())



        c = Canvas("relatorio.pdf")

        c.drawString(50,800,"Paroquia santo antonio")
        zera = 0
        valor = r.valor_recebido
        r.valor_recebido=10
        mes = str(r.mes_referente)
        ps50=  str(p50)
        t50 = str(tamanho50)
        c.drawString(50,750,"Mes da receita")
        c.drawString(50,725,mes[5]+mes[6])
        c.drawString(150,750,"Valor da receita")
        c.drawString(150,725,str(valor))
        c.drawString(250, 750,"Contribuintes ate 50")
        c.drawString(250, 725,t50)
        if tamanhoP_50==0:
            c.drawString(400, 750,"Contribuintes acima de 50")
            c.drawString(400, 725,str(zera))
        else:
            p_50 = pessoa_valor_branco.objects.get(pk=pessoa_valor_branco.objects.all())
            ps_50 = str(p_50)
            t_50 =tamanho_50
            c.drawString(400, 750,"Contribuintes acima de 50")
            c.drawString(400, 725,str(t_50))

        c.save()
        c.showPage()