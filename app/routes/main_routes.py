from flask import Blueprint, jsonify

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/', methods=['GET'])
def principal():
    mensaje = {'mensaje': 'Bienvenido'}
    return jsonify(mensaje)


@main_routes.errorhandler(404)
def page_not_found(e):
    mensaje = {'error': 'Página no encontrada'}
    return jsonify(mensaje), 404
