from app import db, ma
from marshmallow_sqlalchemy import fields
from .usuario import Usuario


class Docente(db.Model):
    __tablename__ = 'docente'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship(Usuario, backref='docente')


class DocenteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Docente
        # exclude = ('id',)
        # ordered = False

    id = ma.auto_field()
    # idUsuario = ma.Int(attribute='id_usuario')
    id_usuario = ma.auto_field()
    usuario = fields.Nested('UsuarioSchema')
