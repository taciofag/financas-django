from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('despesas/', views.despesas_list, name='despesas_list'),
    path('despesas/adicionar/', views.adicionar_despesa, name='adicionar_despesa'),
    path('receitas/', views.receitas_list, name='receitas_list'),
    path('receitas/adicionar/', views.adicionar_receita, name='adicionar_receita'),
]