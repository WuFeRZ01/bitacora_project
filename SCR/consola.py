from SCR.supervisor import Supervisor
from SCR.actividad import Actividad

supervisor = Supervisor()

def menu():
    while True:
        print("\n--- Menú de Gestión de Bitácora ---")
        print("1. Listar actividades")
        print("2. Agregar actividad")
        print("3. Eliminar actividad")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            actividades = supervisor.listar_actividades()
            for i, act in enumerate(actividades):
                print(f"{i}. {act}")

        elif opcion == '2':
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            fecha = input("Fecha: ")
            actividad = Actividad(nombre, descripcion, fecha)
            supervisor.agregar_actividad(actividad)
            print("Actividad agregada exitosamente.")

        elif opcion == '3':
            indice = int(input("Índice a eliminar: "))
            supervisor.eliminar_actividad(indice)
            print("Actividad eliminada.")

        elif opcion == '4':
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == '__main__':
    menu()