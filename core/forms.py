from django import forms
from .models import Receita, Despesa

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['data', 'valor', 'origem', 'descricao']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'origem': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['data', 'valor', 'categoria', 'forma_pagamento', 'descricao', 'pago']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'pago': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
