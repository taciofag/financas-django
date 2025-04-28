from django.contrib import admin
from .models import Categoria, Origem, Receita, Despesa, FormaPagamento, Instituicao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Origem)
class OrigemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'valor', 'origem', 'descricao')
    list_filter = ('origem', 'data')
    search_fields = ('descricao',)

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'valor', 'categoria', 'forma_pagamento', 'pago')
    list_filter = ('categoria', 'forma_pagamento', 'pago', 'data')
    search_fields = ('descricao',)

@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'instituicao')
    search_fields = ('nome',)

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)