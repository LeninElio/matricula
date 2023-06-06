from flask import Blueprint, jsonify

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/', methods=['GET'])
def principal():
    mensaje = {'mensaje': 'Bienvenido'}
    return jsonify(mensaje)
