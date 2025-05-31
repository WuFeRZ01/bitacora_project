from flask import Flask, jsonify, request
from SCR.actividad import Actividad
from SCR.supervisor import Supervisor

app = Flask(__name__)

# Instancias
supervisor = Supervisor()

@app.route('/')
def index():
    return "<h1>Bienvenido al sistema de gestión de bitácoras</h1>"

# ---- ACTIVIDADES ----
@app.route('/actividades', methods=['GET'])
def listar_actividades():
    actividades = supervisor.listar_actividades()
    return jsonify([act.to_dict() for act in actividades])

@app.route('/actividad', methods=['POST'])
def agregar_actividad():
    datos = request.get_json()
    actividad = Actividad(**datos)
    supervisor.agregar_actividad(actividad)
    return jsonify({"mensaje": "Actividad agregada exitosamente"}), 201

@app.route('/actividad/<int:indice>', methods=['DELETE'])
def eliminar_actividad(indice):
    supervisor.eliminar_actividad(indice)
    return jsonify({"mensaje": "Actividad eliminada correctamente"})

# ---- USUARIOS ----
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(supervisor.listar_usuarios())

@app.route('/usuario', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()
    supervisor.agregar_usuario(datos)
    return jsonify({"mensaje": "Usuario agregado correctamente"}), 201

@app.route('/usuario/<int:indice>', methods=['DELETE'])
def eliminar_usuario(indice):
    supervisor.eliminar_usuario(indice)
    return jsonify({"mensaje": "Usuario eliminado correctamente"})

if __name__ == '__main__':
    app.run(debug=True)