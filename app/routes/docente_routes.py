from flask import Blueprint, request, jsonify
from app.controllers.docente_controller import DocenteController

docente_routes = Blueprint('docente_routes', __name__)


@docente_routes.route('/', methods=['POST'])
def create():
    data = request.json
    docente = DocenteController.create(data)
    return jsonify(docente)


@docente_routes.route('/', methods=['GET'])
def read():
    docentes = DocenteController.read()
    return jsonify(docentes)


@docente_routes.route('/<int:id>', methods=['GET'])
def docente_solo(id):
    docente = DocenteController.read_one(id)
    if docente:
        return jsonify(docente)
    else:
        return jsonify({'error': f'El docente {id} no existe.'}), 404


@docente_routes.route('/todos', methods=['GET'])
def todos():
    docentes = DocenteController.todos()
    return jsonify(docentes)
