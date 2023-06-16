"""
Modulo para el manejo de usuarios.
"""

from werkzeug.security import generate_password_hash
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from app.models import usuario_schema, usuarios_schema
from app.utils import validacion
from app.models.alumno import Usuario
from app import db


class UsuarioController:
    """
    Controlador de usuario.
    """

    @staticmethod
    def crear(data):
        """
        Esta función crea un nuevo usuario en una base de datos después de validar los datos 
        de entrada y verificar si hay correo electrónico y nombre de usuario duplicados.
        
        :param data: El parámetro de datos es un diccionario que contiene información sobre 
        un usuario que se está creando.
        :return: ya sea un mensaje de error o los datos de un usuario recién creado.
        """
        try:
            validate(instance=data, schema=validacion.schema)
        except ValidationError:
            return {'error': 'Hay valores no admitidos en los datos.'}

        correo = Usuario.query.filter_by(email=data['email']).first()
        username = Usuario.query.filter_by(username=data['username']).first()

        if correo:
            return {'error': 'El correo electrónico ya está en uso'}

        if username:
            return {'error': 'El nombre de usuario ya está en uso'}

        usuario = Usuario(
            nombre=data['nombre'],
            apellido_paterno=data['apellido_paterno'],
            apellido_materno=data['apellido_materno'],
            email=data['email'],
            sexo=data['sexo'],
            username=data['username'],
            password=generate_password_hash(data['password'])
        )

        db.session.add(usuario)
        db.session.commit()
        return usuario_schema.dump(usuario)

    @staticmethod
    def usuarios_todos():
        """
        Esta función recupera todos los usuarios de la base de datos y los devuelve como 
        un objeto JSON serializado mediante un esquema.
        :return: La función `usuarios_todos()` devuelve una lista de todos los usuarios de 
        la base de datos.
        """
        usuarios = Usuario.query.all()
        return usuarios_schema.dump(usuarios)

    @staticmethod
    def un_usuario(id_usuario):
        """
        La función recupera un objeto de usuario de la base de datos y devuelve su representación
        serializada mediante un esquema.
        
        :param id: El parámetro "id" es una variable que representa el identificador de un usuario
        en la base de datos.
        :return: La función `un_user` devuelve la representación serializada de un objeto 
        `Usuario` con el `id` dado, utilizando el esquema `user_schema`.
        """
        usuario = Usuario.query.get(id_usuario)
        return usuario_schema.dump(usuario)

    @staticmethod
    def eliminar_usuario(id_usuario):
        """
        Esta función elimina un usuario de la base de datos en función de su ID.

        :param id: El parámetro "id" es el identificador del usuario que debe eliminarse de la
        base de datos.
        """
        usuario = Usuario.query.get(id_usuario)
        db.session.delete(usuario)
        db.session.commit()

    @staticmethod
    def actualizar_usuario(id_usuario, data):
        """
        Esta función actualiza la información de un usuario en la base de datos, validando los
        datos de entrada y verificando nombres de usuario duplicados.
        
        :param id: El parámetro id es el identificador único del usuario que debe actualizarse en la
        base de datos
        :param data: El parámetro de datos es un diccionario que contiene la información actualizada
        para un usuario.
        :return: Si hay un error de validación, la función devuelve un diccionario con una clave de
        'error' y un mensaje que indica que hay valores no permitidos en los datos.
        """
        try:
            validate(instance=data, schema=validacion.schema)
        except ValidationError:
            return {'error': 'Hay valores no admitidos en los datos.'}

        usuario = Usuario.query.get(id_usuario)
        if 'username' in data and data['username'] != usuario.username:
            username = Usuario.query.filter_by(username=data['username']).first()
            if username:
                return {'error': 'El nombre de usuario ya esta en uso.'}

        for key in data:
            if key != 'password':
                setattr(usuario, key, data[key])
        db.session.commit()
        return usuario.to_dict()
