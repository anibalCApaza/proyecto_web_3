from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from proyecto.models import Proyecto
from tarea.models import Tarea


# Create your views here.
def ver_tarea(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tareas = Tarea.objects.filter(proyecto=proyecto)

    return render(
        request,
        "tarea/ver_tarea.html",
        {
            "proyecto": proyecto,
            "tareas": tareas,
        },
    )


@login_required 
def crear_tarea(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)

    if request.method == "POST":
        form = Tarea(request.POST)
        if form.is_valid():
            Tarea = form.save(commit=False)
            Tarea.proyecto = proyecto
            Tarea.creador_en = request.user
            Tarea.save()
            return redirect("ver_proyecto", id=id_proyecto)
    else:
        form = Tarea()

    return render(
        request,
        "tarea/crear_tarea.html",
        {
            "form": form,
            "proyecto": proyecto,
        },
    )

def crear_etiqueta(request):
    return HttpResponse(
        b"Esta vista muestra un formulario en caso de una peticion GET, si es POST valida los datos de la nueva etiqueta y la registra,es importante considerar que entre estos datos debe figurar el id de la tarea al que se agregara esta etiqueta"
    )
