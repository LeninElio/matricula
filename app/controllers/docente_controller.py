from app import db
from app.models.docente import Docente
from app.models.usuario import Usuario
from app.models import docente_schema, docentes_schema
from app.controllers.usuario_controller import UsuarioController


class DocenteController:

    # @staticmethod
    # def create(data):
    #     docente = Docente(id_usuario=data['id_usuario'])
    #     db.session.add(docente)
    #     db.session.commit()
    #     return docente_schema.dump(docente)

    @staticmethod
    def create(data):
        usuario = Usuario.query.filter_by(email=data['email']).first()
        if usuario:
            return {"Error": "El correo ya existe."}

        else:
            usuario_data = {
                'nombre': data['nombre'],
                'email': data['email']
            }
            usuario = UsuarioController.create(usuario_data)
            docente = Docente(id_usuario=usuario['id'])
            db.session.add(docente)
            db.session.commit()
            return docente_schema.dump(docente)

    @staticmethod
    def read():
        docentes = Docente.query.all()
        return docentes_schema.dump(docentes)

    @staticmethod
    def read_one(id):
        docente = Docente.query.get(id)
        return docente_schema.dump(docente)

    @staticmethod
    def todos():
        docentes = Docente.query.join(Usuario, Docente.id_usuario == Usuario.id).all()
        return docentes_schema.dump(docentes)
