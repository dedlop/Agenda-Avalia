from django.shortcuts import render
from .models import Paciente, Consulta
from .forms import PacienteForm, ConsultaForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    """Página principal da Agenda Avalia"""
    #Busca todas consultas de todos pacientes no banco de dados
    now = timezone.now()
    consultas = Consulta.objects.filter(data__gte=now.date()).order_by('data', 'hora')
    return render(request, 'agenda_pacientes/index.html', {'consultas': consultas})

@login_required
def pacientes(request):
    """Mostra todos pacientes"""
    pacientes = Paciente.objects.filter(owner=request.user).order_by('date_added')
    context = {'pacientes': pacientes}
    return render(request, 'agenda_pacientes/pacientes.html', context)

@login_required
def novo_paciente(request):
    """Adiciona novo paciente"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = PacienteForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = PacienteForm(request.POST)
        if form.is_valid():
            novo_paciente = form.save(commit=False)
            novo_paciente.owner = request.user
            novo_paciente.save()
            return HttpResponseRedirect(reverse('pacientes'))
    
    context = {'form': form}
    return render(request, 'agenda_pacientes/novo_paciente.html', context)

@login_required
def consultas(request, paciente_id):
    """Mostra lista de consultas do paciente"""
    paciente = Paciente.objects.get(id = paciente_id)

    # Garante que a consulta pertence ao usuário atual
    if paciente.owner != request.user:
        raise Http404

    horarios = paciente.consulta_set.order_by('id')
    context = {'paciente': paciente, 'horarios': horarios}
    return render(request, 'agenda_pacientes/consultas.html', context)

@login_required
def nova_consulta(request, paciente_id):
    """Agenda uma nova consulta"""
    paciente = Paciente.objects.get(id = paciente_id)

    # Garante que a consulta pertence ao usuário atual
    if paciente.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = ConsultaForm()

    else:
        # Dados de POST submetidos; processa os dados
        form = ConsultaForm(data=request.POST)
        if form.is_valid():
            nova_consulta = form.save(commit=False)
            nova_consulta.paciente = paciente
            nova_consulta.save()
            return HttpResponseRedirect(reverse('consultas', args=[paciente_id]))
        
    context = {'paciente': paciente, 'form': form}
    return render(request, 'agenda_pacientes/nova_consulta.html', context)

@login_required
def editar_consulta(request, consulta_id):
    """Edita uma consulta existente"""
    consulta = Consulta.objects.get(id=consulta_id)
    paciente = consulta.paciente

    # Garante que a consulta pertence ao usuário atual
    if paciente.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Requisição inicial; preenche previamente o formulário com a entrada atual
        form = ConsultaForm(instance=consulta)

    else:
        # Dados de Post submetidos; processa os dados
        form = ConsultaForm(instance=consulta, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('consultas', args=[paciente.id]))
        
    context = {'consulta': consulta, 'paciente': paciente, 'form': form}
    
    return render(request, 'agenda_pacientes/editar_consulta.html', context)