from django.contrib import admin

from models import *

admin.site.register(pessoa)
admin.site.register(receita_ate_50)
admin.site.register(receita_maior_50)
admin.site.register(despesa)
admin.site.register(Emcaixa)

