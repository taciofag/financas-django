from django.shortcuts import render, redirect
from .models import Receita, Despesa
from .forms import ReceitaForm, DespesaForm
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth
from itertools import chain
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    todas_receitas = Receita.objects.all()
    todas_despesas = Despesa.objects.all()

    ano = request.GET.get('ano')
    mes = request.GET.get('mes')

    receitas = todas_receitas
    despesas = todas_despesas

    if ano and mes:
        receitas = receitas.filter(data__year=ano, data__month=mes)
        despesas = despesas.filter(data__year=ano, data__month=mes)

    saldo = (receitas.aggregate(Sum('valor'))['valor__sum'] or 0) - (despesas.aggregate(Sum('valor'))['valor__sum'] or 0)

    # Anos e meses baseados em todas receitas e despesas
    anos_receitas = todas_receitas.annotate(year=ExtractYear('data')).values_list('year', flat=True)
    anos_despesas = todas_despesas.annotate(year=ExtractYear('data')).values_list('year', flat=True)
    anos = sorted(set(chain(anos_receitas, anos_despesas)))

    meses_receitas = todas_receitas.annotate(month=ExtractMonth('data')).values_list('month', flat=True)
    meses_despesas = todas_despesas.annotate(month=ExtractMonth('data')).values_list('month', flat=True)
    meses_numericos = sorted(set(chain(meses_receitas, meses_despesas)))
    meses = [f"{m:02d}" for m in meses_numericos]

    # 🎯 Gastos por categoria baseado apenas nas despesas filtradas
    gastos_por_categoria = despesas.filter(categoria__isnull=False) \
        .values('categoria__nome') \
        .annotate(total=Sum('valor')) \
        .filter(total__gt=0) \
        .order_by('-total')

    labels = [g['categoria__nome'] for g in gastos_por_categoria]
    valores = [float(g['total']) for g in gastos_por_categoria]

    context = {
        'saldo': saldo,
        'receitas': receitas,
        'despesas': despesas,
        'meses': meses,
        'anos': anos,
        'ano': ano,
        'mes': mes,
        'labels': labels,
        'valores': valores,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def despesas_list(request):
    despesas = Despesa.objects.all()
    return render(request, 'core/despesas_list.html', {'despesas': despesas})

@login_required
def receitas_list(request):
    receitas = Receita.objects.all()
    return render(request, 'core/receitas_list.html', {'receitas': receitas})

@login_required
def adicionar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita cadastrada com sucesso!')
            return redirect('receitas_list')
    else:
        form = ReceitaForm()
    return render(request, 'core/adicionar_receita.html', {'form': form})

@login_required
def adicionar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Despesa cadastrada com sucesso!')
            return redirect('despesas_list')
    else:
        form = DespesaForm()
    return render(request, 'core/adicionar_despesa.html', {'form': form})
