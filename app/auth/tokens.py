from datetime import datetime, timedelta
import uuid
import jwt

JWT_SECRET_KEY = 'my_secret_key'


def generate_token(user_id, expiration_days=7): # pylint: disable=missing-docstring
    now = datetime.utcnow()

    expiration = now + timedelta(days=expiration_days)
    payload = {
        'sub': user_id,
        'iat': now,
        'jti': str(uuid.uuid4()),
        'exp': expiration
    }

    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return token
