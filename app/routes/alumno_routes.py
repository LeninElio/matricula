from flask import Blueprint, request, jsonify
from app.controllers.alumno_controller import AlumnoController

alumno_routes = Blueprint('alumno_routes', __name__)


@alumno_routes.route('/', methods=['POST'])
def create():
    data = request.json
    alumno = AlumnoController.create(data)
    return jsonify(alumno)


@alumno_routes.route('/', methods=['GET'])
def read():
    alumnos = AlumnoController.read()
    return jsonify(alumnos)


@alumno_routes.route('/<int:id>', methods=['GET'])
def solo(id):
    alumno = AlumnoController.solo(id)
    return jsonify(alumno)
