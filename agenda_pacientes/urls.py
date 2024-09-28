from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('novo_paciente', views.novo_paciente, name='novo_paciente'),
    path('consultas/<paciente_id>/', views.consultas, name='consultas'),
    path('nova_consulta/<paciente_id>', views.nova_consulta, name='nova_consulta'),
    path('editar_consulta/<consulta_id>', views.editar_consulta, name='editar_consulta'),
]
