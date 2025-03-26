# Django con PostgreSQL usando Docker

Este repositorio proporciona una configuración básica para integrar Django con una base de datos PostgreSQL utilizando Docker y Docker Compose. Permite un entorno containerizado tanto para la aplicación Django como para la base de datos PostgreSQL, facilitando el proceso de desarrollo y despliegue.

### Dependencias

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

### Configuración del Proyecto

1. **Clonar el repositorio:**

   Clona el repositorio en tu máquina local:

   git clone https://github.com/tu_usuario/django-postgres-docker.git
   cd django-postgres-docker

### 2. Construir e iniciar los contenedores:

Utiliza Docker Compose para construir e iniciar los contenedores requeridos. Esto configurará tanto la aplicación Django como los contenedores de la base de datos PostgreSQL:

docker-compose up --build


### 3. Acceder a la aplicación Django:

Después de que los contenedores estén en funcionamiento, accede a la aplicación Django desde tu navegador en:

http://localhost:8000


### 4. Ejecutar las migraciones de la base de datos:

Una vez que los contenedores estén activos, ejecuta las migraciones de Django para inicializar la base de datos PostgreSQL:

docker-compose exec web python manage.py migrate


### 5. Crear un superusuario (opcional):

Si es necesario, crea un superusuario para acceder a la interfaz de administración de Django:

docker-compose exec web python manage.py createsuperuser


Sigue las indicaciones para crear una cuenta de superusuario.

###Estructura del Proyecto
docker-compose.yml: Define los servicios (Django y PostgreSQL) y sus configuraciones.

Dockerfile: Especifica las instrucciones para construir el contenedor de Django.

requirements.txt: Lista los paquetes Python requeridos, incluyendo Django y psycopg2.

app/: Directorio de la aplicación Django que contiene configuraciones, modelos, vistas, etc.

###Configuración
PostgreSQL: La base de datos está configurada con las siguientes credenciales (configuradas en docker-compose.yml):

Usuario: django
Contraseña: password
Base de datos: mi_db

Estas credenciales se utilizan en la configuración DATABASES dentro del archivo settings.py del proyecto Django.

### Despliegue
Para el despliegue, esta configuración puede ser extendida a cualquier proveedor de la nube o servicio de hosting que soporte Docker, como AWS, DigitalOcean o Heroku. Ajusta las variables de entorno y las configuraciones de conexión de la base de datos en los archivos docker-compose.yml y settings.py según sea necesario para entornos de producción.

### 🤝 Contribuye
Si tienes una idea para mejorar este proyecto, ¡sería genial contar con tu aporte! Haz un fork, comparte tus mejoras y envía un pull request. ¡Toda ayuda es bienvenida! 🚀

