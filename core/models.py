from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Origem(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Origens'

class Receita(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    origem = models.ForeignKey(Origem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.origem.nome} - R$ {self.valor}'

class Despesa(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    forma_pagamento = models.CharField(max_length=50)
    pago = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.categoria.nome} - R$ {self.valor}'

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Instituições'

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} ({self.instituicao.nome})'
    
    class Meta:
        verbose_name_plural = 'Formas de Pagamento'

class Despesa(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    pago = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.categoria.nome} - R$ {self.valor}'
