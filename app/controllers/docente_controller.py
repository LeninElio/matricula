from app import db
from app.models.docente import Docente
from app.models.usuario import Usuario
from app.models import docente_schema, docentes_schema


class DocenteController:
    @staticmethod
    def create(data):
        docente = Docente(id_usuario=data['id_usuario'])
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
