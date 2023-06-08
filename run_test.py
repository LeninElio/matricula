# class UsuarioSchema(ma.Schema):
#     nombreUsuario = ma.Str(attribute='nombre')
#     emailUsuario = ma.Str(attribute='email')

data = {'nombre': 'juan'}

if 'nombre' in data:
    print(data['nombre'])
else:
    print('no hay')
