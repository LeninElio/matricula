from functools import wraps
import jwt
from flask import request, abort, session, make_response, jsonify
from app.auth.tokens import JWT_SECRET_KEY
from app.models.usuario import Usuario


def requires_auth(func): # pylint: disable=missing-docstring
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return {'error': 'El usuario no ha iniciado sesion.'}

        user = Usuario.query.get(user_id)
        if not user or not user.is_admin:
            response = make_response(jsonify(message="Debe ser un usuario administrador."), 401)
            abort(response)

        token = request.headers.get('Authorization')
        if not token:
            response = make_response(jsonify(message="Fallo en la autorizacion del token."), 401)
            abort(response)

        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('sub')
            if not user_id:
                response = make_response(jsonify(message="Fallo en la decodificacion."), 401)
                abort(response)

            user = Usuario.query.get(user_id)
            if not user:
                response = make_response(jsonify(message="El usuario no existe."), 401)
                abort(response)

        except jwt.ExpiredSignatureError:
            response = make_response(jsonify(message="Token expirado."), 401)
            abort(response)

        except (jwt.InvalidTokenError, Exception): # pylint: disable=broad-except
            response = make_response(jsonify(message="Token invalido."), 401)
            abort(response)

        return func(*args, **kwargs)

    return wrapper
