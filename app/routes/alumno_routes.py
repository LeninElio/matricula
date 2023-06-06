from flask import Blueprint, request, jsonify
from app.models.alumno import Alumno
from app.controllers.alumno_controller import AlumnoController

alumno_routes = Blueprint('alumno_routes', __name__)


@alumno_routes.route('/create', methods=['POST'])
def crear():
    data = request.json
    alumno = AlumnoController.crear(data)
    return jsonify(alumno)


@alumno_routes.route('/', methods=['GET'])
def alumnos_todos():
    alumnos = AlumnoController.alumnos_todos()
    return jsonify(alumnos)


@alumno_routes.route('/<int:id>', methods=['GET'])
def un_alumno(id):
    alumno = AlumnoController.un_alumno(id)
    return jsonify(alumno)


@alumno_routes.route('/<int:id>', methods=['DELETE'])
def eliminar_alumno(id):
    alumno = Alumno.query.get(id)
    if alumno is None:
        return jsonify({'error': 'Alumno no encontrado.'}), 404
    AlumnoController.eliminar_alumno(id)
    return jsonify({'message': 'Alumno eliminado.'}), 200
