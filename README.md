# PASOS DE INSTALACIÓN DEL PROYECTO

- Clonar el repositorio

```terminal
git clone https://github.com/anibalCApaza/my_nvim_config
```

- Se debe crear un entorno virtual en tu computadora

```terminal
python -m venv venv
```

- activar el entorno virtual
  En Windows:

```terminal
venv\Scripts\activate
```

- Instalar las dependencias que se encuentran en el archivo 'requirements.txt' con:

```python
pip install -r requirements.txt
```

- Ejecutar el servidor con:

```python
python manage.py runserver
```

## REQUERIMIENTOS DEL SISTEMA

**TIPO DE SISTEMA:** Gestor de tareas en equipo

**TABLAS:** Proyecto, Tarea, Usuario, Etiqueta
**FUNCIONALIDADES:**

- Asignar tareas.
- Estado de las tareas(pendiente/completado)
- Notificaciones

## NOTAS PARA TRABAJAR CON EL REPOSITORIO

- Actualiza tu repositorio local con el de github cada vez que vayas a trabajar con el proyecto:

```git
git pull
```

- No tocar la rama **"main"** , debes crear una rama alterna y trabajar en ella todos los cambios que vayas a realizar
- Toda solicitud de modificación debe ser a través de 'Pull Requests'
- Todo módulo o funcionalidad debe ir acorde al apartado de requerimientos.
- Notificar por whatsapp cuando terminen una funcionalidad en sus ramas, para revisar las mismas y fusionar sus cambios.
