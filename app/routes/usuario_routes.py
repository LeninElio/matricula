from flask import Blueprint, request, jsonify
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
