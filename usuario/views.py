from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registrarse(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, "usuario/registroUsuario.html")
        if User.objects.filter(username=usuario).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return render(request, "usuario/registroUsuario.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado.")
            return render(request, "usuario/registroUsuario.html")

        User.objects.create_user(
            username=usuario,
            email=email,
            password=password1,
            first_name=nombre,
            last_name=apellido,
        )
        messages.success(request, "Registro correcto. Ahora puedes iniciar sesión.")
        return redirect("usuario:iniciar_sesion")
    else:
        return render(request, "usuario/registroUsuario.html")


def iniciar_sesion(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        contrasenia = request.POST["password"]
        user = authenticate(request, username=usuario, password=contrasenia)

        if user is not None:
            login(request, user)
            return redirect("proyecto:index")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, "usuario/inicioSesion.html")
    else:
        return render(request, "usuario/inicioSesion.html")


def mostrar_usuario(request):
    if request.user.is_authenticated:
        nombre = request.user.username
    else:
        nombre = ""
    return render(request, "usuario/mostrarUsuario.html", {"usuario": nombre})


def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect("proyecto:index")
