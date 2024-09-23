from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('pacientes/<paciente_id>/', views.paciente, name='paciente'),
    path('novo_paciente', views.novo_paciente, name='novo_paciente'),
]
