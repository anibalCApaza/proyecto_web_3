from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from proyecto.forms import ProyectoForm
from .models import Proyecto


# TODO: Considera que todas las vistas deben usar return render....... para mostrar su información en un template


def index(request):
    context = {
        "description": "Gestor de tarea en equipo: Organizar proyectos y colabora con tu equipo.",
    }
    return render(request, "proyecto/index.html", context)


@login_required
def lista_proyecto(request):
    proyectos = Proyecto.objects.all()

    return render(request, "proyecto/lista_proyecto.html", {"proyectos": proyectos})


@login_required
def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario_crea = request.user
            proyecto.save()
            return redirect("lista_proyectos")
    else:
        form = ProyectoForm()

    context = {
        "form": form,
    }
    return render(request, "proyecto/crear_proyecto.html", context)


@login_required
def ver_proyecto(request, id):
    pass
