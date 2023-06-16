"""
Este módulo define el modelo y el esquema para la entidad Docente.
"""

from marshmallow_sqlalchemy import fields
from app import db, ma
from .usuario import Usuario


class Docente(db.Model):
    """
    Define la tabla Docente en la base de datos.
    """
    __tablename__ = 'docente'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship(Usuario, backref='docente')


class DocenteSchema(ma.SQLAlchemySchema):
    """
    Define el esquema para serializar y deserializar instancias de Docente.
    """
    class Meta:
        model = Docente
        # exclude = ('id',)
        # ordered = False

    id = ma.auto_field()
    # idUsuario = ma.Int(attribute='id_usuario')
    id_usuario = ma.auto_field()
    usuario = fields.Nested('UsuarioSchema')
