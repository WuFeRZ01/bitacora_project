import tkinter as tk
from SCR.supervisor import Supervisor
from SCR.actividad import Actividad

supervisor = Supervisor()

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Bitácoras")

        self.label = tk.Label(root, text="Nombre Actividad:")
        self.label.pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        self.label_desc = tk.Label(root, text="Descripción:")
        self.label_desc.pack()
        self.entry_desc = tk.Entry(root)
        self.entry_desc.pack()

        self.label_fecha = tk.Label(root, text="Fecha:")
        self.label_fecha.pack()
        self.entry_fecha = tk.Entry(root)
        self.entry_fecha.pack()

        self.boton_agregar = tk.Button(root, text="Agregar Actividad", command=self.agregar_actividad)
        self.boton_agregar.pack()

        self.boton_listar = tk.Button(root, text="Listar Actividades", command=self.mostrar_actividades)
        self.boton_listar.pack()

        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.pack()

    def agregar_actividad(self):
        nombre = self.entry_nombre.get()
        desc = self.entry_desc.get()
        fecha = self.entry_fecha.get()
        act = Actividad(nombre, desc, fecha)
        supervisor.agregar_actividad(act)
        self.resultado.insert(tk.END, "Actividad agregada\n")

    def mostrar_actividades(self):
        self.resultado.delete(1.0, tk.END)
        for act in supervisor.listar_actividades():
            self.resultado.insert(tk.END, str(act) + "\n")

if __name__ == '__main__':
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
