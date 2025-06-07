from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Considera que todas las views deben mostrar html, por que se tiene que usar return render.........

#Plantilla Registro
def registro(request):
    return render(request,'usuario/registroUsuario.html')
#Vista para registrarUsuarios
def registrarse(request):
    User.objects.create_user(
            username=request.POST['usuario'],
            email=request.POST['email'],
            password=request.POST['password1'],
            first_name=request.POST['nombre'],
            last_name=request.POST['apellido']
        )
    return redirect('/usuario/registro')
#Plantilla Inicio sesion
def iniciar_sesion(request):
    return render(request,'usuario/inicioSesion.html',{'error':''})
#Vista para iniciar sesion
def inicio_sesion(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        contrasenia = request.POST['password']
        user = authenticate(request, username=usuario, password=contrasenia)
        
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                nombre = request.user.username
            return render(request, 'usuario/mostrarUsuario.html',{'usuario':nombre})
        else:
            return render(request, 'usuario/inicioSesion.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
#Plantilla para mostrar usuario
def mostrar_usuario(request):
    if request.user.is_authenticated:
        nombre = request.user.username
    else: 
        nombre=""
    return render(request, 'usuario/mostrarUsuario.html',{'usuario':nombre})

def cerrar_sesion(request):
    logout(request)
    return render(request, 'usuario/inicioSesion.html',{'error':''})
