from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import EtiquetaForm, TareaForm
from django.contrib.auth.models import User
from random import choice
from proyecto.models import Proyecto
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "tarea/listaTareas.html", {"tareas": tareas})


@login_required
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
    colores = ["verde-malanchite", "amarillo-auerolin", "texto-azul", "rojo-persa","egg-blue","corn-blue"];
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            Tarea = form.save(commit=False)
            Tarea.color = choice(colores)
            Tarea.proyecto = proyecto
            Tarea.creador_en = request.user
            Tarea.save()
            return redirect("proyecto:ver_proyecto", id=id_proyecto)
    else:
        form = TareaForm()

    return render(
        request,
        "tarea/crear_tarea.html",
        {
            "form": form,
            "proyecto": proyecto,
        },
    )


@login_required
def crear_etiqueta(request):
    return HttpResponse(
        b"Esta vista muestra un formulario en caso de una peticion GET, si es POST valida los datos de la nueva etiqueta y la registra,es importante considerar que entre estos datos debe figurar el id de la tarea al que se agregara esta etiqueta"
    )


@login_required
def agregar_etiqueta(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = EtiquetaForm(request.POST)
        if form.is_valid():  # valida el formulario
            etiqueta = form.save(
                commit=False
            )  # no se guarda por que falta adicionar datos
            etiqueta.tarea = tarea
            etiqueta.save()
            return redirect("proyecto:ver_proyecto", id=tarea.proyecto_id)
    else:
        form = EtiquetaForm()
    return render(
        request, "tarea/agregar_etiqueta.html", {"form": form, "tarea": tarea, "proyecto": tarea.proyecto}
    )


@login_required
def asignar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == "POST":
        usuario_id = request.POST.get("usuario_id")

        if usuario_id:  # Si se seleccionó un usuario
            usuario = get_object_or_404(
                User, id=usuario_id
            )  # ¡Aquí se usa el User importado!
            tarea.asignado_a = usuario
        else:  # Si se eligió desasignar
            tarea.asignado_a = None

        tarea.save()

    return redirect("proyecto:ver_proyecto", tarea.proyecto_id)


@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("proyecto:ver_proyecto", tarea.proyecto_id)
    else:
        form = TareaForm(instance=tarea)

    return render(
        request,
        "tarea/editar_tarea.html",
        {
            "form": form,
            "tarea": tarea,
            "proyecto": tarea.proyecto,  # Para mantener consistencia con crear_tarea
        },
    )