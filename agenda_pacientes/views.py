from django.shortcuts import render
from .models import Paciente
from .forms import PacienteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """Página principal da Agenda Avalia"""
    return render(request, 'agenda_pacientes/index.html')

def pacientes(request):
    """Mostra todos pacientes"""
    pacientes = Paciente.objects.order_by('date_added')
    context = {'pacientes': pacientes}
    return render(request, 'agenda_pacientes/pacientes.html', context)

def paciente(request, paciente_id):
    """Mostra os dados e horários do paciente"""
    paciente = Paciente.objects.get(id = paciente_id)
    dados = paciente.dados_set.order_by('-date_added')
    context = {'paciente': paciente, 'dados': dados}
    return render(request, 'agenda_pacientes/paciente.html', context)

def novo_paciente(request):
    """Adiciona novo paciente"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = PacienteForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pacientes'))
    
    context = {'form': form}
    return render(request, 'agenda_pacientes/novo_paciente.html', context)