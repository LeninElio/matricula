from flask import request, session
from app.auth.auth import authenticate
from app.auth.tokens import generate_token

def login(): # pylint: disable=missing-docstring
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')

        user = authenticate(username, password)

        if user:
            session['user_id'] = user.id
            access_token = generate_token(user.id)

            return {'user': user.to_dict()} | {"access_token": access_token}
        return {'error': 'Usuario o contraseña inválidos'}
    return {'error': 'Metodo de solicitud no válida.'}
