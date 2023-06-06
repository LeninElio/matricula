from app import db
from app.models.docente import Docente
from app.models.usuario import Usuario
from app.models import docente_schema, docentes_schema
from app.controllers.usuario_controller import UsuarioController


class DocenteController:

    @staticmethod
    def crear(data):
        usuario = Usuario.query.filter_by(email=data['email']).first()
        if usuario:
            return {"Error": "El correo ya existe."}

        else:
            usuario_data = {
                'nombre': data['nombre'],
                'email': data['email']
            }
            usuario = UsuarioController.crear(usuario_data)
            docente = Docente(id_usuario=usuario['id'])
            db.session.add(docente)
            db.session.commit()
            return docente_schema.dump(docente)

    @staticmethod
    def docentes_todos():
        docentes = Docente.query.all()
        return docentes_schema.dump(docentes)

    @staticmethod
    def un_docente(id):
        docente = Docente.query.get(id)
        return docente_schema.dump(docente)

    @staticmethod
    def eliminar_docente(id):
        docente = Docente.query.get(id)
        db.session.delete(docente)
        db.session.commit()
