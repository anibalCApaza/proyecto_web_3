from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from proyecto.forms import ProyectoForm
from tarea.models import Etiqueta, Tarea
from .models import MiembroProyecto, Proyecto


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
    proyecto = get_object_or_404(Proyecto, id=id)
    tareas = Tarea.objects.filter(proyecto_id=id)
    miembros = MiembroProyecto.objects.filter(proyecto_id=id)
    etiquetas = Etiqueta.objects.all()
    context = {
        "proyecto": proyecto,
        "tareas": tareas,
        "miembros": miembros,
        "etiquetas": etiquetas,
    }
    return render(request, "proyecto/ver_proyecto.html", context=context)

def agregar_usuario(request,id):
    proyecto = get_object_or_404(Proyecto, id=id)
    usuario_actual=request.user
    error=''
    miembros_ids = MiembroProyecto.objects.filter(proyecto=proyecto).values_list('usuario_agregado_id', flat=True)
    usuarios=User.objects.exclude(id__in=miembros_ids).exclude(id=usuario_actual.id)
    if request.method=="POST":
        username_usuario=request.POST['username']
        nombre_usuario=request.POST['nombre']
        try:
            usuario=User.objects.get(username=username_usuario,first_name=nombre_usuario)
            if usuario.id == usuario_actual.id or usuario.id in miembros_ids:
                error='No puedes agregar a este usuario'
            else:
                MiembroProyecto.objects.create(proyecto=proyecto, usuario_agregado=usuario)
                return redirect('proyecto:ver_proyecto', id=proyecto.id)
        except User.DoesNotExist:
            error='Error usuario no encontrado'
    else:
        pass
    context={"usuarios":usuarios,'proyecto':proyecto,'error':error}
    return render(request,"proyecto/agregar_usuario.html", context=context)