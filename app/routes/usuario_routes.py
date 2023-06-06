from flask import Blueprint, request, jsonify
from app.controllers.usuario_controller import UsuarioController

usuario_routes = Blueprint('usuario_routes', __name__)


@usuario_routes.route('/create', methods=['POST'])
def create():
    data = request.json
    usuario = UsuarioController.create(data)
    return jsonify(usuario)


@usuario_routes.route('/', methods=['GET'])
def read():
    usuarios = UsuarioController.read()
    return jsonify(usuarios)
