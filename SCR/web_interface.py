# Este archivo sería un cliente básico para probar las rutas del web_controller
import requests

BASE_URL = "http://127.0.0.1:5000"

print("Listado de actividades:")
res = requests.get(f"{BASE_URL}/actividades")
print(res.json())

print("Agregando actividad nueva:")
nueva_actividad = {
    "nombre": "Revisión de planos",
    "descripcion": "Revisar planos arquitectónicos de la obra",
    "fecha": "2025-05-31"
}
res = requests.post(f"{BASE_URL}/actividad", json=nueva_actividad)
print(res.json())

print("Listado actualizado:")
res = requests.get(f"{BASE_URL}/actividades")
print(res.json())