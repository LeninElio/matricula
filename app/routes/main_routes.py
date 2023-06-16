"""
Modulo de redireccionamiento principal.
"""

from flask import Blueprint, jsonify

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/', methods=['GET'])
def principal():
    """
    La función devuelve un objeto JSON con un mensaje de bienvenida.
    :return: La función `principal()` devuelve un objeto JSON que contiene el mensaje 
    "Bienvenido" como valor asociado a la clave "mensaje".
    """
    mensaje = {'mensaje': 'Bienvenido'}
    return jsonify(mensaje)
