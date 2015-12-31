from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paroquial.views.home', name='home'),
    # url(r'^paroquial/', include('paroquial.foo.urls')),
    url(r'^inicial/$','app_paroquia_oaf.views.apresentacao'),
    url(r'^receita_ate_50/$','app_paroquia_oaf.views.receitas'),
    url(r'^receita_maior_50/$','app_paroquia_oaf.views.receitass'),
    url(r'^pessoa/$','app_paroquia_oaf.views.pessoas'),
    url(r'^pessoa_valor_branco/$','app_paroquia_oaf.views.pessoas_valor_em_branco'),
    url(r'^despesas/$','app_paroquia_oaf.views.despesas'),
    url(r'^em_caixa/$','app_paroquia_oaf.views.valor_caixa'),
    url(r'^lista_pessoas/$','app_paroquia_oaf.views.lista_pessoas'),
    url(r'^relatorio/$','app_paroquia_oaf.views.relatorio'),
    #url(r'^lista_pessoas/(?P<nr_item>\d+)/$','app_paroquia_oaf.views.lista_pessoas'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$','django.contrib.auth.views.login', {"template_name":"login.html"}),
    url(r'^logout/$','django.contrib.auth.views.logout_then_login',{'login_url':'/'})
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
