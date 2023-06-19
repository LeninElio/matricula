"""
Modulo para el manejo de las rutas del usuario.
"""

from flask import Blueprint, request, jsonify
from app.models.usuario import Usuario
from app.models.docente import Docente
from app.models.alumno import Alumno
from app.controllers.usuario_controller import UsuarioController

usuario_routes = Blueprint('usuario_routes', __name__)


@usuario_routes.route('/create', methods=['POST'])
def crear():
    """
    Esta función crea un nuevo usuario tomando datos de una solicitud y usando un UserController
    para crear el usuario.
    :return: La función `crear()` devuelve una respuesta JSON que contiene los datos de un usuario
    recién creado. Los datos del usuario se obtienen del JSON de solicitud y se pasan al método
    `UsuarioController.crear()`, que crea el usuario y devuelve sus datos. La función `jsonify()`
    se usa para convertir los datos del usuario a un formato JSON que se puede enviar como 
    respuesta al cliente.
    """
    data = request.json
    usuario = UsuarioController.crear(data)
    return jsonify(usuario)


@usuario_routes.route('/', methods=['GET'])
def usuarios_todos():
    """
    Esta función recupera todos los usuarios y los devuelve en formato JSON.
    :return: una representación JSON de todos los usuarios del sistema.
    """
    usuarios = UsuarioController.usuarios_todos()
    return jsonify(usuarios)


@usuario_routes.route('/<int:id_usuario>', methods=['GET'])
def un_usuario(id_usuario):
    """
    Esta función recupera a un usuario por su ID y devuelve su información en formato JSON,
    o devuelve un mensaje de error si el usuario no existe.
    
    :param id: El parámetro "id" es una variable que representa el identificador único de
    un usuario. Se  utiliza como entrada a la función "un_usuario" para recuperar la información del 
    usuario de la base de datos. Si el usuario existe, la función devuelve la información del
    usuario en formato JSON.
    :return: Si el usuario con el `id` dado existe, la función devuelve una representación JSON del
    usuario. Si el usuario no existe, la función devuelve un objeto JSON con un mensaje de 
    error y un código de estado 404.
    """
    usuario = UsuarioController.un_usuario(id_usuario)
    if usuario:
        return jsonify(usuario)
    return jsonify({'error': f'El usuario {id_usuario} no existe.'}), 404


@usuario_routes.route('/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    """
    Esta función elimina a un usuario del sistema, pero solo si no está designado como docente o
    estudiante.
    
    :param id: El parámetro "id" es el identificador único del usuario que debe eliminarse
    del sistema.
    :return: una respuesta JSON con un mensaje que indica si el usuario se eliminó correctamente
    o si hubo un error. Si el usuario es designado como docente o alumno, la función devuelve 
    un mensaje de error con un código de estado de 409 (Conflicto). Si no se encuentra el usuario, 
    la función devuelve un mensaje de error con un código de estado de 404 (No encontrado).
    """
    usuario = Usuario.query.get(id_usuario)
    docente = Docente.query.filter_by(id=id_usuario).first()
    alumno = Alumno.query.filter_by(id=id_usuario).first()

    if docente is not None:
        return jsonify({'error': 'El usuario esta designado como docente, primero eliminelo.'}), 409

    if alumno is not None:
        return jsonify({'error': 'El usuario esta designado como alumno, primero eliminelo.'}), 409

    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado.'}), 404

    UsuarioController.eliminar_usuario(id_usuario)
    return jsonify({'message': 'Usuario eliminado.'}), 200


@usuario_routes.route('/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    """
    Esta función actualiza la información de un usuario en una base de datos utilizando datos de una
    solicitud JSON.
    
    :param id: El parámetro id es el identificador único del usuario que debe actualizarse
    :return: una respuesta JSON con los datos de usuario actualizados y un código de estado de 200.
    """
    data = request.get_json()
    usuario = UsuarioController.actualizar_usuario(id_usuario, data)
    return jsonify(usuario), 200
