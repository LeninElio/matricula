from flask import Blueprint, request, jsonify
from app.models.docente import Docente
from app.controllers.docente_controller import DocenteController

docente_routes = Blueprint('docente_routes', __name__)


@docente_routes.route('/create', methods=['POST'])
def crear():
    data = request.json
    docente = DocenteController.crear(data)
    return jsonify(docente)


@docente_routes.route('/', methods=['GET'])
def docentes_todos():
    docentes = DocenteController.docentes_todos()
    return jsonify(docentes)


@docente_routes.route('/<int:id>', methods=['GET'])
def un_docente(id):
    docente = DocenteController.un_docente(id)
    if docente:
        return jsonify(docente)
    else:
        return jsonify({'error': f'El docente {id} no existe.'}), 404


@docente_routes.route('/<int:id>', methods=['DELETE'])
def eliminar_docente(id):
    docente = Docente.query.get(id)
    if docente is None:
        return jsonify({'error': 'Docente no encontrado.'}), 404
    DocenteController.eliminar_docente(id)
    return jsonify({'message': 'Docente eliminado.'}), 200


@docente_routes.route('/<int:id>', methods=['PUT'])
def actualizar_docente(id):
    data = request.get_json()
    docente = DocenteController.actualizar_docente(id, data)
    if docente.get('error') is not None:
        return docente
    else:
        id_usuario = Docente.query.filter_by(id_usuario=docente['id']).first()
        return DocenteController.un_docente(id_usuario.id)
