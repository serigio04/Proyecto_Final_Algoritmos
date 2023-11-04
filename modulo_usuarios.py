import tkinter as tk

class Usuario():
    def __init__(self, id, nombre, contraseña):
        self.id = id
        self.nombre = nombre
        self.contraseña =  contraseña
usuarios = []

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
    def registrar_usuario():
        name = entrada_u_agregar_nombre.get()
        password = entrada_u_agregar_contraseña.get()
        if name and password:
            id_user = len(usuarios) + 1
            new_user = Usuario(id_user, name, password)
            with open("C:/Archivos/Grupo4/Usuarios.txt", "a") as archivo_usuarios:
                archivo_usuarios.write(f"{new_user.id},{new_user.nombre},{new_user.contraseña}\n")
        usuarios.append(new_user)

    boton_registrar_u = tk.Button(frame_u_agregar, text="Registrar usuario", command=registrar_usuario)
    boton_registrar_u.pack()

    return frame_u_agregar


def eliminar_usuario(frame):
    frame_u_eliminar = tk.Frame(frame)

    def mostrar_usuarios():
        usuarios_disponibles.delete("1.0", tk.END)
        usuarios_disponibles.insert(tk.END, "Usuarios:\n")
        with open("C:/Archivos/Grupo4/Usuarios.txt", "r") as archivo_u:
            usuarios = archivo_u.readlines()
            for usuario in usuarios:
                id, nombre, contraseña = usuario.strip().split(',')
                usuarios_disponibles.insert(tk.END, f"ID: {id}, Nombre: {nombre}\n")
                
    boton_mostrar_usuarios = tk.Button(frame_u_eliminar, text="Mostrar usuarios disponibles", command=mostrar_usuarios)
    boton_mostrar_usuarios.pack()
    usuarios_disponibles = tk.Text(frame_u_eliminar, width=70, height=10)
    usuarios_disponibles.pack()
    label_u_eliminar_id = tk.Label(frame_u_eliminar, text="ID del usuario a eliminar:")
    entrada_u_eliminar_id = tk.Entry(frame_u_eliminar)
    label_u_eliminar_id.pack()
    entrada_u_eliminar_id.pack()

    def eliminar_usuario():
        id_a_eliminar = entrada_u_eliminar_id.get()
        with open("C:/Archivos/Grupo6/Usuarios.txt", "r") as archivo_u:
            usuarios = archivo_u.readlines()

        usuarios_actualizados = []
        usuario_eliminado = False
        for usuario in usuarios:
            id, nombre, contraseña = usuario.strip().split(',')
            if id != id_a_eliminar:
                usuarios_actualizados.append(usuario)
            else:
                usuario_eliminado = True

        if usuario_eliminado:
            with open("C:/Archivos/Grupo6/Usuarios.txt", "w") as archivo_u:
                archivo_u.writelines(usuarios_actualizados)
            mostrar_usuarios()

    boton_eliminar_usuario = tk.Button(frame_u_eliminar, text="Eliminar usuario por ID", command=eliminar_usuario)
    boton_eliminar_usuario.pack()

    return frame_u_eliminar


def modificar_usuario(frame):
    frame_u_modificar = tk.Frame(frame)
    label_u_modificar_nombre = tk.Label(frame_u_modificar, text="Nombre: (usuario)")
    label_u_modificar_contraseña = tk.Label(frame_u_modificar, text="Contraseña: ")
    entrada_u_modificar_nombre = tk.Entry(frame_u_modificar)
    entrada_u_modificar_contraseña = tk.Entry(frame_u_modificar)

    label_u_modificar_nombre.pack()
    entrada_u_modificar_nombre.pack()
    label_u_modificar_contraseña.pack()
    entrada_u_modificar_contraseña.pack()
    return frame_u_modificar