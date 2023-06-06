from app import db, ma
from marshmallow_sqlalchemy import fields
from .usuario import Usuario


class Alumno(db.Model):
    __tablename__ = 'alumno'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship(Usuario, backref='alumno')


class AlumnoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Alumno
        # exclude = ('id',)
        # ordered = False

    id = ma.auto_field()
    id_usuario = ma.auto_field()
    usuario = fields.Nested('UsuarioSchema')
