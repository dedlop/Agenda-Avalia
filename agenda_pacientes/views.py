from django.shortcuts import render
from .models import Paciente

def index(request):
    """Página principal da Agenda Avalia"""
    return render(request, 'agenda_pacientes/index.html')

def pacientes(request):
    """Mostra todos pacientes"""
    pacientes = Paciente.objects.order_by('date_added')
    context = {'pacientes': pacientes}
    return render(request, 'agenda_pacientes/pacientes.html', context)
