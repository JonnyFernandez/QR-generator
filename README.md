# Configuracion

---

1. Instalar entorno virtual: `pip install virtualenv`
2. Comprobar entorno: `virtualenv --version`
3. Crear entorno virtual dentro del proyecto: `virtualenv venv`
4. Activar el entorno virtual: `.\venv\Scripts\activate`
5. Instalar las dependencias: `pip install -r requirements.txt`
6. Crear requirement.txt: `pip freeze > requirements.txt
`

# Installar Django

1. Instalar Django: `pip install django`
2. Ver la version de Django: `django-admin --version`
3. Mostrar paquetes de Python: `pip list`

# Creacion de Proyecto Django

1. Iniciar un proyecto: `django-admin startproject mysite .`
2. Levantar server :`python manage.py runserver`
3. Cambiar de puerto (Op): `python manage.py runserver 3001`
4. Info: `python manage.py --help`

# Creacion de Carpeta

1. Creacion de apps: `Python manage.py startapp "nombre de app"`

# PARA TRABAJAR CON SQLite

Creando tablas y migrándolas a sqlite

1. Python manage.py makemigrations (opcional :"nombre de la app")
2. Python manage.py migrate
