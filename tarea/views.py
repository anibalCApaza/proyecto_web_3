from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Team, Task


# Create your views here.
def ver_tarea(request, id):
    proyecto = get_object_or_404(Team, id=id)
    tareas = Task.objects.filter(project=proyecto).order_by('-created_at')
    
    return render(request, 'tasks/ver_tarea.html', {
        'proyecto': proyecto,
        'tareas': tareas,
    })


@login_required
def crear_tarea(request, project_id):
    project = get_object_or_404(Team, id=project_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project  
            task.creator = request.user  
            task.save()
            return redirect('ver_proyecto', id=project_id)  
    else:
        form = TaskForm()
    
    return render(request, 'tasks/crear_tarea.html', {
        'form': form,
        'project': project,
    })


def crear_etiqueta(request):
    return HttpResponse(
        b"Esta vista muestra un formulario en caso de una peticion GET, si es POST valida los datos de la nueva etiqueta y la registra,es importante considerar que entre estos datos debe figurar el id de la tarea al que se agregara esta etiqueta"
    )
