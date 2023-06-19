from datetime import datetime, timedelta
import jwt

JWT_SECRET_KEY = 'mysecretkey'


def generate_token(user_id, expiration_days=7): # pylint: disable=missing-docstring
    # Obtener la fecha y hora actual
    now = datetime.utcnow()

    # Calcular la fecha y hora de expiración del token
    expiration = now + timedelta(days=expiration_days)

    # Crear el payload del token
    payload = {
        'sub': user_id,
        'iat': now,
        'exp': expiration
    }

    # Generar el token JWT
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')
