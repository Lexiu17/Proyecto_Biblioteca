# Proyecto_Biblioteca
Proyecto de una aplicacion para el control de una biblioteca
Aplicación web en Django para el control de una biblioteca: libros, autores, editoriales y préstamos, con registro de usuarios, grupos y permisos.

**Autor:** [CENTENO SAHID ]
**Tema asignado:** Control de biblioteca
**Materia:** Programación II, UTE

## Modelo de datos

Cuatro tablas relacionadas:

| Tabla | Campos principales | Relaciones |
|---|---|---|
| Editorial | nombre, país, fundación | Tiene muchos libros |
| Autor | nombre, nacionalidad, fecha de nacimiento | Muchos a muchos con Libro |
| Libro | título, isbn, año, precio, creado_por | ForeignKey a Editorial (PROTECT), ManyToMany con Autor, ForeignKey a User |
| Prestamo | nombre_lector, fechas, estado (TextChoices), creado_por | ForeignKey a Libro (CASCADE), ForeignKey a User |

```
Editorial 1 ──── N Libro N ──── N Autor
                    │
                    1
                    │
                    N
                 Prestamo
```

## Cómo levantar el proyecto desde cero

```bash
git clone [https://github.com/Lexiu17/Proyecto_Biblioteca]
cd biblioteca-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos
python manage.py runserver
```

En Linux o Mac, la activación es `source venv/bin/activate`.

La aplicación queda en http://127.0.0.1:8000/ y el administrador en http://127.0.0.1:8000/admin/.

## Datos de prueba

El comando `python manage.py cargar_datos` crea los grupos `administradores` y `consultores` con sus permisos, 5 registros en cada tabla y los usuarios de prueba. Se puede ejecutar varias veces sin duplicar datos.

## Usuarios de prueba

| Usuario | Contraseña | Grupo | Qué puede hacer |
|---|---|---|---|
| nenata | 12345 | Superusuario | Todo, incluido el admin de Django |
| admin1 | 12345admin | administradores | Crear, editar y eliminar en las cuatro entidades |
| lector1 | lect12345 | consultores | Ver todo, crear libros y editar solo los que creó |

Los usuarios que se registran en `/registro/` entran automáticamente al grupo `consultores`.