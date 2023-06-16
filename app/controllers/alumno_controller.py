"""
Modulo para el manejo de alumnos.
"""

from app import db
from app.models.alumno import Alumno
from app.models import alumno_schema, alumnos_schema
from app.controllers.usuario_controller import UsuarioController


class AlumnoController:
    """
    Controlador de alumno.
    """

    @staticmethod
    def crear(data):
        """
        Esta función crea un nuevo usuario y lo agrega como estudiante en la base de datos.
        
        :param data: Es un diccionario que contiene los datos necesarios para crear un nuevo
        usuario.
        :return: Si el diccionario `usuario` devuelto por `UsuarioController.crear(data)` 
        tiene una clave de error, entonces se devuelve ese error. De lo contrario, se crea 
        un objeto `Alumno`.
        """
        usuario = UsuarioController.crear(data)
        if usuario.get('error') is not None:
            return usuario

        alumno = Alumno(id_usuario=usuario['id'])
        db.session.add(alumno)
        db.session.commit()
        return alumno_schema.dump(alumno)

    @staticmethod
    def alumnos_todos():
        """
        Esta función recupera todos los estudiantes de la base de datos.
        :return: La función `alumnos_todos()` devuelve una lista de todos los objetos 
        `Alumno` en la base de datos.
        """
        alumnos = Alumno.query.all()
        return alumnos_schema.dump(alumnos)

    @staticmethod
    def un_alumno(id_alumno):
        """
        La función elimina a un estudiante de la base de datos usando su ID.
        
        :param id_alumno: El parámetro `id_alumno` es el identificador único del estudiante 
        que debe eliminarse de la base de datos
        :return: La función `un_alumno` devuelve los datos de un estudiante con el `id_alumno` 
        dado al consultar la base de datos y usar `alumno_schema` para serializar los datos. 
        La función `eliminar_alumno` no devuelve nada, simplemente elimina a un alumno de la
        base de datos.
        """
        alumno = Alumno.query.get(id_alumno)
        return alumno_schema.dump(alumno)

    @staticmethod
    def eliminar_alumno(id_alumno):
        """
        Esta función elimina a un estudiante de la base de datos usando su ID.
        
        :param id_alumno: El parámetro `id_alumno` es el identificador único del estudiante que debe
        eliminarse de la base de datos
        """
        alumno = Alumno.query.get(id_alumno)
        db.session.delete(alumno)
        db.session.commit()

    @staticmethod
    def actualizar_alumno(id_alumno, data):
        """
        Esta función actualiza la información de un estudiante llamando a una función para
        actualizar la información del usuario.
        
        :param id_alumno: El id del alumno a actualizar
        :param data: El parámetro "datos" es un diccionario que contiene la información 
        actualizada para el estudiante.
        :return: resultado de llamar a la función `actualizar_usuario` desde la clase
        `UsuarioController` con los parámetros `id_usuario` y `data`. Si el `id_usuario` 
        es `Ninguno`, devuelve un diccionario con un mensaje de error indicando que el 
        usuario no existe.
        """
        id_usuario = Alumno.query.get(id_alumno)
        if id_usuario is None:
            return {'error': 'El usuario no existe.'}

        actualiza_alumno = UsuarioController.actualizar_usuario(id_usuario.id_usuario, data)
        return actualiza_alumno
