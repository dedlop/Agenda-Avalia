from django.shortcuts import render

def index(request):
    """Página principal da Agenda Avalia"""
    return render(request, 'agenda_pacientes/index.html')
