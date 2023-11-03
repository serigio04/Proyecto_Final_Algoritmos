import tkinter as tk

class Usuario():
    def __init__(self, id, nombre, contraseña):
        self.id = id
        self.nombre = nombre
        self.contraseña =  contraseña

usuarios = []

archivo_u = open("C:/Archivos/Grupo4/Usuarios.txt")
archivo_usuarios = archivo_u.readlines()

i = 1
for user in archivo_u:
    datos = user.strip().split(",")
    i = datos[0]
    nombre = datos[1]
    contraseña = datos[2]
    registro = Usuario(i,nombre,contraseña)
    i += 1
    usuarios.append(registro)

def agregar_usuario(frame):
    frame_u_agregar = tk.Frame(frame)
    label_u_agregar_nombre = tk.Label(frame_u_agregar, text="Nombre: (usuario)")
    label_u_agregar_contraseña = tk.Label(frame_u_agregar, text="Contraseña: ")
    entrada_u_agregar_nombre = tk.Entry(frame_u_agregar)
    entrada_u_agregar_contraseña = tk.Entry(frame_u_agregar)

    label_u_agregar_nombre.pack()
    entrada_u_agregar_nombre.pack()
    label_u_agregar_contraseña.pack()
    entrada_u_agregar_contraseña.pack()
    return frame_u_agregar

# lo de abajo no me sirvio jajaja

# def registrar_usuario():
#     name = agregar_usuario.entrada_u_agregar_nombre.get()
#     password = agregar_usuario.entrada_u_agregar_contraseña.get()
#     user = Usuario(i,name,password)
#     usuarios.append(user)
# boton_add_user = tk.Button(agregar_usuario.frame_u_agregar, text="Agregar usuario", command=registrar_usuario)
# boton_add_user.pack()

def eliminar_usuario():
    pass

def modificar_usuario():
    pass
