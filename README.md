# API de Gestión de Mesas y Sesiones de D&D

Esta es una API RESTful para gestionar usuarios, DMs (Dungeon Masters), partidas y personajes en el contexto de Dungeons & Dragons (D&D), creada con Django y Django Rest Framework (DRF). Permite realizar operaciones CRUD sobre los siguientes recursos:

- **Usuarios**: Gestiona la información de los jugadores, incluyendo su nombre, apodo, correo electrónico y rol (novato o administrador).
- **Dungeon Masters (DMs)**: Permite gestionar a los DMs que dirigen las partidas, incluyendo su relación con las mesas de juego.
- **Partidas**: Administra las mesas de juego, sus sistemas, estados y reglas.
- **Personajes**: Permite crear y gestionar personajes, incluyendo sus atributos, niveles y modificadores.

Con esta API, los usuarios pueden interactuar con todos los aspectos de sus sesiones de D&D de manera eficiente y organizada.

## Tabla de Contenidos

- [API de Gestión de Mesas y Sesiones de D\&D](#api-de-gestión-de-mesas-y-sesiones-de-dd)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Características](#características)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)

## Características

- Crear, leer, actualizar y eliminar usuarios.
- Crear, leer, actualizar y eliminar DMs (Dungeon Masters).
- Crear, leer, actualizar y eliminar partidas.
- Crear, leer, actualizar y eliminar personajes.
- Validación de atributos de personajes, incluyendo niveles y modificadores.
- Soporte para atributos de modificadores en formato JSON.

## Requisitos

- Python 3.6 o superior
- Django 3.2 o superior
- Django Rest Framework 3.12 o superior

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Crea un entorno virtual (opcional pero recomendado)**:

  ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
  ```

3. **Instala las dependencias**:
  ```bash
    pip install -r requirements.txt
  ```

4. **Realiza las migraciones de la base de datos**:
  ```bash
    python manage.py migrate
  ```

5. **Crea un superusuario (opcional, para acceder al panel de administración)**:
  ```bash
    python manage.py createsuperuser
  ```

6. **Inicia el servidor de desarrollo**:
  ```bash
    python manage.py runserver
  ```

7. **Acceder a la documentacion del proyecto**:
- Ahi que dirigirse a la url [Documentacion](http://127.0.0.1:8000/docs)