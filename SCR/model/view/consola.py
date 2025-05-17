from SRC.controller.usuario_controller import UsuarioController
from SRC.controller.actividad_controller import ActividadController


def consola():
    controlador_usuario = UsuarioController()
    usuario = None

    while not usuario:
        print("1. Registrar\n2. Iniciar sesión")
        op = input("Seleccione una opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            try:
                controlador_usuario.registrar_usuario(nombre, correo, contraseña)
                print("Usuario registrado.")
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            try:
                usuario = controlador_usuario.iniciar_sesion(correo, contraseña)
                print("Inicio de sesión exitoso.")
            except Exception as e:
                print("Error:", e)

    controlador_actividad = ActividadController(usuario.id)
    while True:
        print("\n1. Crear actividad\n2. Ver actividades\n3. Salir")
        op = input("Opción: ")
        if op == "1":
            descripcion = input("Descripción: ")
            responsable = input("Responsable: ")
            condiciones = input("Condiciones climáticas: ")
            fecha = input("Fecha y hora: ")
            controlador_actividad.crear_actividad(descripcion, responsable, condiciones, fecha)
            print("Actividad creada.")
        elif op == "2":
            actividades = controlador_actividad.listar_actividades()
            for act in actividades:
                print(f"- {act.descripcion} ({act.fecha_hora})")
        elif op == "3":
            break
