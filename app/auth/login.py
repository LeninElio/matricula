from flask import request, session
from app.auth.auth import authenticate

def login(): # pylint: disable=missing-docstring
    if request.method == 'POST':
        # Obtener los datos ingresados por el usuario
        username = request.json.get('username')
        password = request.json.get('password')

        # Autenticar al usuario
        user = authenticate(username, password)

        if user:
            # Crear una sesión de usuario
            session['user_id'] = user.id

            # Retornar los datos del usuario autenticado en formato JSON
            return {'user': user.to_dict()}
        # Si las credenciales son inválidas, retornar un mensaje de error en formato JSON
        return {'error': 'Usuario o contraseña inválidos'}
    # Si la solicitud no es POST, retornar un mensaje de error en formato JSON
    return {'error': 'Solicitud no válida'}
