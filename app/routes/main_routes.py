"""
Modulo de redireccionamiento principal.
"""

from flask import Blueprint, jsonify, session
from app.models.usuario import Usuario
from app.auth.login import login
from app.utils.auth import requires_auth

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/login', methods=['POST'])
def user_login():
    """
    Funcion para el inicio de session.
    """
    return login()


@main_routes.route('/logout')
def logout():
    """
    Eliminar la sesión de usuario
    """
    session.pop('user_id', None)
    mensaje = {'message': 'Sesión cerrada exitosamente'}
    return jsonify(mensaje)


@main_routes.route('/', methods=['GET'])
@main_routes.route('/home', methods=['GET'])
@requires_auth
def home():
    """
    :return: La función `home()` devuelve un objeto JSON de bienvenida
    """
    user_id = session.get('user_id')
    if not user_id:
        mensaje = {'error': 'Debe iniciar session.'}
        return jsonify(mensaje)

    user = Usuario.query.get(user_id)
    mensaje = {'message': f'Bienvenido {user.nombre}'}
    return jsonify(mensaje)
