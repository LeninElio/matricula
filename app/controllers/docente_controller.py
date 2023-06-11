from app import db
from app.models.docente import Docente
from app.models import docente_schema, docentes_schema
from app.controllers.usuario_controller import UsuarioController


class DocenteController:

    @staticmethod
    def crear(data):
        usuario = UsuarioController.crear(data)
        if usuario.get('error') is not None:
            return usuario

        else:
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

    @staticmethod
    def actualizar_docente(id, data):
        id_usuario = Docente.query.get(id)
        actualiza_usuario = UsuarioController.actualizar_usuario(id_usuario.id_usuario, data)
        return actualiza_usuario
