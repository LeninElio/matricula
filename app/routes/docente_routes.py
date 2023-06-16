"""
Modulo para el manejo de las rutas del docente.
"""

from flask import Blueprint, request, jsonify
from app.models.docente import Docente
from app.controllers.docente_controller import DocenteController

docente_routes = Blueprint('docente_routes', __name__)


@docente_routes.route('/create', methods=['POST'])
def crear():
    """
    Esta función crea un nuevo docente (profesor) utilizando datos de una solicitud JSON y 
    devuelve el docente creado como una respuesta JSON.
    :return: una respuesta JSON que contiene los datos del objeto "docente" recién creado.
    """
    data = request.json
    docente = DocenteController.crear(data)
    return jsonify(docente)


@docente_routes.route('/', methods=['GET'])
def docentes_todos():
    """
    Esta función recupera todos los profesores y los devuelve en formato JSON.
    :return: una representación JSON de todos los "docentes" (maestros) obtenidos del módulo
    "DocenteController".
    """
    docentes = DocenteController.docentes_todos()
    return jsonify(docentes)


@docente_routes.route('/<int:id>', methods=['GET'])
def un_docente(id_docente):
    """
    Esta función recupera la información de un profesor específico y la devuelve como un objeto 
    JSON, o devuelve un mensaje de error si el profesor no existe.
    
    :param id: El parámetro "id" es una variable que representa el identificador único de un 
    docente en el sistema. Se utiliza para recuperar información sobre un docente específico de 
    la base de datos a través del método DocenteController.un_docente().
    :return: Si el docente existe, se devuelve una representación JSON del docente. Si el docente no
    existe, se devuelve un objeto JSON con un mensaje de error y un código de estado 404.
    """
    docente = DocenteController.un_docente(id_docente)
    if docente:
        return jsonify(docente)
    return jsonify({'error': f'El docente {id} no existe.'}), 404


@docente_routes.route('/<int:id>', methods=['DELETE'])
def eliminar_docente(id_docente):
    """
    Esta función elimina un objeto Docente de la base de datos por su ID y devuelve una 
    respuesta JSON.
    
    :param id: El parámetro "id" es el identificador único del docente (profesor) que necesita ser
    eliminado de la base de datos
    :return: Si no se encuentra el docente, se devuelve una respuesta JSON con un mensaje de 
    error y un código de estado 404. Si se encuentra el docente y se elimina con éxito, se devuelve 
    una respuesta JSON con un mensaje de éxito y un código de estado 200.
    """
    docente = Docente.query.get(id_docente)
    if docente is None:
        return jsonify({'error': 'Docente no encontrado.'}), 404
    DocenteController.eliminar_docente(id_docente)
    return jsonify({'message': 'Docente eliminado.'}), 200


@docente_routes.route('/<int:id_docente>', methods=['PUT'])
def actualizar_docente(id_docente):
    """
    Esta función actualiza al docente y devuelve los datos actualizados.

    :param id: El ID del docente (profesor) a actualizar
    :return: resultado de llamar al método `un_docente` de la clase `DocenteController` con el
    `id_usuario` del objeto `Docente` actualizado como argumento.
    """
    data = request.get_json()
    docente = DocenteController.actualizar_docente(id_docente, data)
    if docente.get('error') is not None:
        return docente

    id_usuario = Docente.query.filter_by(id_usuario=docente['id']).first()
    return DocenteController.un_docente(id_usuario.id)
