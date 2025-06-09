from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Task
from proyecto.models import Team
from .forms import TeamCreationForm 


# TODO: Considera que todas las vistas deben usar return render....... para mostrar su información en un template


def index(request):
    context = {
        'description': "Gestor de tarea en equipo: Organizar proyectos y colabora con tu equipo.",
    }
    return render(request, 'index.html', context)

@login_required
def lista_proyecto(request):
    proyectos = Proyecto.objects.filter(creator=request.user).orden_by('-start_date')

    return render(request, 'proyecto/lista_proyecto.html', {
        'proyectos': proyectos
    })


@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.creator = request.user
            proyecto.save()
            return redirect('lista_proyecto')
    else:
        form = TeamCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'proyecto/crear_proyecto.html', context)

@login_required
def ver_proyecto(request, id):
    proyecto = get_object_or_404(Team, id=id, creator=request.user)
    tareas = Task.objects.filter(team=proyecto).order_by('-created_at')
    
    return render(request, 'proyecto/ver_proyecto.html', {
        'proyecto': proyecto,
        'tareas': tareas,
    })
