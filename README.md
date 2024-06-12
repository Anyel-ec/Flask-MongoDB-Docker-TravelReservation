# Flask User Management App

Este es un proyecto de aplicación web utilizando Flask para la gestión de usuarios. Incluye funcionalidades de creación, lectura, actualización y eliminación (CRUD) de usuarios. La aplicación utiliza MongoDB como base de datos.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)
- MongoDB

## Instalación

### Clonar el repositorio

```sh
git clone https://github.com/Anyel-ec/Flask-MongoDB-Docker-TravelReservation
cd Flask-MongoDB-Docker-TravelReservation
```

### Crear y activar un entorno virtual

```sh
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows
```

### Instalar dependencias

```sh
pip install -r requirements.txt
```

### Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```env
DB_NAME=nombre_de_tu_base_de_datos
DB_URL=mongodb://localhost:27017/
```

### Ejecutar la aplicación

```sh
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Estructura del Proyecto

```
flask-user-management/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── UserController.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── Environment.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── User.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── UserRepository.py
│   └── services/
│       ├── __init__.py
│       └── UserService.py
└── templates/
    ├── index.html
    ├── User/
        ├── crear_usuario.html
        ├── ver_usuario.html
        ├── actualizar_usuario.html
        └── index.html
```

## Endpoints

### Página de Inicio de Sesión

```
GET / 
```

### Crear un Nuevo Usuario

```
GET /usuarios/nuevo
POST /usuarios/nuevo
```

### Ver Detalles de un Usuario

```
GET /usuarios/<email>
```

### Editar un Usuario

```
GET /usuarios/<email>/editar
POST /usuarios/<email>/editar
```

### Eliminar un Usuario

```
POST /usuarios/<email>/eliminar
```

### Listar Todos los Usuarios

```
GET /usuarios
```

## Dependencias

Las dependencias del proyecto están listadas en el archivo `requirements.txt`:

```
blinker==1.8.2
click==8.1.7
colorama==0.4.6
dnspython==2.6.1
Flask==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
pymongo==4.7.3
python-dotenv==1.0.1
Werkzeug==3.0.3
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con tus mejoras.

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](https://opensource.org/licenses/MIT).
```

Este `README.md` cubre los aspectos esenciales de tu proyecto, incluyendo la instalación, estructura del proyecto, endpoints disponibles y dependencias. Puedes ajustarlo según las necesidades específicas de tu proyecto.