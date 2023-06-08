from flask import Blueprint, request, jsonify
from app.models.usuario import Usuario
from app.models.docente import Docente
from app.models.alumno import Alumno
from app.controllers.usuario_controller import UsuarioController

usuario_routes = Blueprint('usuario_routes', __name__)


@usuario_routes.route('/create', methods=['POST'])
def crear():
    data = request.json
    usuario = UsuarioController.crear(data)
    return jsonify(usuario)


@usuario_routes.route('/', methods=['GET'])
def usuarios_todos():
    usuarios = UsuarioController.usuarios_todos()
    return jsonify(usuarios)


@usuario_routes.route('/<int:id>', methods=['GET'])
def un_usuario(id):
    usuario = UsuarioController.un_usuario(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'error': f'El usuario {id} no existe.'}), 404


@usuario_routes.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    docente = Docente.query.filter_by(id_usuario=id).first()
    alumno = Alumno.query.filter_by(id_usuario=id).first()

    if docente is not None:
        return jsonify({'error': 'El usuario esta designado como docente, primero eliminelo.'}), 409

    if alumno is not None:
        return jsonify({'error': 'El usuario esta designado como alumno, primero eliminelo.'}), 409

    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado.'}), 404

    UsuarioController.eliminar_usuario(id)
    return jsonify({'message': 'Usuario eliminado.'}), 200


@usuario_routes.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    usuario = UsuarioController.actualizar_usuario(id, data)
    return jsonify(usuario.to_dict()), 200
