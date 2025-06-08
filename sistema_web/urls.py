"""
URL configuration for sistema_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function include1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ...existing code...
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuario/", include(("usuario.urls", "usuario"), namespace="usuario")),
    path("proyecto/", include("proyecto.urls")),
    path("tarea/", include("tarea.urls")),
    # ...existing code...

]
