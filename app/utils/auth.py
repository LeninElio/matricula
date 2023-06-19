from functools import wraps
import jwt
from flask import request, abort, session
from app.auth.tokens import JWT_SECRET_KEY
from app.models.usuario import Usuario


def requires_auth(func): # pylint: disable=missing-docstring
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Verificar si el usuario ha iniciado sesión
        user_id = session.get('user_id')
        if not user_id:
            return {'error': 'Fallo en el login.'}

        # Verificar si el usuario tiene los permisos necesarios
        user = Usuario.query.get(user_id)
        if not user or not user.is_admin:
            print('IS ADMIIIIN', user.is_admin)
            abort(401)

        # Verificar si el token de autenticación es válido
        token = request.headers.get('Authorization')
        if not token:
            print('Fallo en el token')
            abort(401)

        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('sub')
            if not user_id:
                abort(401)

            # Verificar si el usuario existe en la base de datos
            user = Usuario.query.get(user_id)
            if not user:
                abort(401)

        except jwt.ExpiredSignatureError:
            abort(401)

        except (jwt.InvalidTokenError, Exception): # pylint: disable=broad-except
            abort(401)

        # Si todas las validaciones son exitosas, llamar a la función original
        return func(*args, **kwargs)

    return wrapper
