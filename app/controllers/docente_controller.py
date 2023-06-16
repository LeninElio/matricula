"""
Modulo para el manejo de docentes.
"""

from app import db
from app.models.docente import Docente
from app.models import docente_schema, docentes_schema
from app.controllers.usuario_controller import UsuarioController


class DocenteController:
    """
    Controlador docente.
    """

    @staticmethod
    def crear(data):
        """
        Esta función crea un nuevo objeto Docente en la base de datos y devuelve su representación
        serializada.
        
        :param data: Es un diccionario que contiene los datos necesarios para crear un nuevo
        usuario.
        :return: Si el diccionario `usuario` tiene una clave de error, entonces se devuelve
        ese error. De lo contrario, se crea un nuevo objeto `Docente`.
        """
        usuario = UsuarioController.crear(data)
        if usuario.get('error') is not None:
            return usuario

        docente = Docente(id_usuario=usuario['id'])
        db.session.add(docente)
        db.session.commit()
        return docente_schema.dump(docente)

    @staticmethod
    def docentes_todos():
        """
        Esta función los devuelve como una lista serializada utilizando el esquema docentes.
        :return: La función devuelve una lista de todos los objetos `Docente` en la base de
        datos.
        """
        docentes = Docente.query.all()
        return docentes_schema.dump(docentes)

    @staticmethod
    def un_docente(id_docente):
        """
        Esta función recupera la información de un maestro específico de una base de datos y 
        la devuelve en un formato serializado usando un esquema.
        
        :param id_docente: . La función `un_docente` toma un parámetro como entrada y lo usa para 
        recuperar el objeto `Docente` correspondiente de la base de datos.
        :return: la representación serializada de un solo objeto Docente con el parámetro 
        `id_docente` dado.
        """
        docente = Docente.query.get(id_docente)
        return docente_schema.dump(docente)

    @staticmethod
    def eliminar_docente(id_docente):
        """
        Esta función elimina un objeto docente específico de la base de datos.
        
        :param id_docente: El parámetro `id_docente` es el identificador de un objeto `Docente`
        en la base de datos. Se utiliza para localizar y eliminar el objeto `Docente`.
        """
        docente = Docente.query.get(id_docente)
        db.session.delete(docente)
        db.session.commit()

    @staticmethod
    def actualizar_docente(id_docente, data):
        """
        Esta función actualiza la información de un docente llamando a una función para 
        actualizar su información de usuario.
        
        :param id_docente: El ID del docente (profesor) que necesita ser actualizado
        :param data: El parámetro data es un diccionario que contiene la información actualizada
        del docente.
        :return: resultado de llamar a la función `actualizar_usuario` desde la clase
        `UsuarioController`.
        """
        id_usuario = Docente.query.get(id_docente)
        if id_usuario is None:
            return {'error': 'El docente no existe.'}

        actualiza_usuario = UsuarioController.actualizar_usuario(id_usuario.id_usuario, data)
        return actualiza_usuario
