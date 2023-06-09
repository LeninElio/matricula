# class UsuarioSchema(ma.Schema):
#     nombreUsuario = ma.Str(attribute='nombre')
#     emailUsuario = ma.Str(attribute='email')
from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "nombre": "Editadooo",
    "apellido_materno": "Patrie editado",
    "apellido_paterno": "Chandler editado",
    "sexo": 0,
    "email": "edit@gmail.com",
    "username": "cspedit",
    "password": "paswordcitoedit"
}

with app.app_context():
    # datos = jsonify(data)
    for key in data:
        print(data[key])
