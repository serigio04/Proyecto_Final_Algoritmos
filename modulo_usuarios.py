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



def eliminar_usuario(usuarios_disponibles, entrada_nombre):
    nombre_a_eliminar = entrada_nombre.get()

    try:
        with open("C:/Archivos/Grupo4/Usuarios.txt", "r") as archivo_usuarios:
            usuarios_registrados = archivo_usuarios.readlines()

        # Abre el archivo en modo escritura "w" para sobrescribirlo
        with open("C:/Archivos/Grupo4/Usuarios.txt", "w") as archivo_usuarios:
            for usuario in usuarios_registrados:
                if not usuario.startswith(nombre_a_eliminar):  # No escribas el usuario a eliminar
                    archivo_usuarios.write(usuario)

        # Muestra la lista de usuarios actualizada
        usuarios_disponibles.delete("1.0", tk.END)
        usuarios_disponibles.insert(tk.END, "Usuarios Registrados:\n")
        for usuario in usuarios_registrados:
            usuarios_disponibles.insert(tk.END, usuario)

    except FileNotFoundError:
        usuarios_disponibles.delete("1.0", tk.END)
        usuarios_disponibles.insert(tk.END, "El archivo de usuarios no existe o está vacío.")

    # Limpia la entrada de nombre después de eliminar
    entrada_nombre.delete(0, tk.END)
    boton_eliminar_usuario = tk.Button(frame_u_eliminar, text="Eliminar usuario", command=lambda: eliminar_usuario(usuarios_disponibles, entrada_u_eliminar_nombre))
    boton_eliminar_usuario.pack()

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

