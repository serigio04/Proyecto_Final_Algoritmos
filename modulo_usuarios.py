import tkinter as tk

class Usuario():
    def __init__(self, id, nombre, contrasenia):
        self.id = id
        self.nombre = nombre
        self.contrasenia =  contrasenia

def mostrar_mensaje(mensaje):
    exito_label = tk.Label(text=mensaje, fg="green")
    exito_label.pack()

def mostrar_mensaje_err(mensaje):
    exito_label = tk.Label(text=mensaje, fg="red")
    exito_label.pack()

def agregar_usuario(frame):
    frame_u_agregar = tk.Frame(frame)
    label_u_agregar_nombre = tk.Label(frame_u_agregar, text="Nombre: (usuario)")
    label_u_agregar_contrasenia = tk.Label(frame_u_agregar, text="contraseña: ")
    entrada_u_agregar_nombre = tk.Entry(frame_u_agregar)
    entrada_u_agregar_contrasenia = tk.Entry(frame_u_agregar)

    label_u_agregar_nombre.pack()
    entrada_u_agregar_nombre.pack()
    label_u_agregar_contrasenia.pack()
    entrada_u_agregar_contrasenia.pack()
    def registrar_usuario():
        name = entrada_u_agregar_nombre.get()
        password = entrada_u_agregar_contrasenia.get()
        if name and password:
            with open("C:/Archivos/Grupo4/Usuarios.txt", "r") as archivo_usuarios:
                usuarios = archivo_usuarios.readlines()

            id_user = len(usuarios) + 1
            new_user = Usuario(id_user, name, password)
            with open("C:/Archivos/Grupo4/Usuarios.txt", "a") as archivo_usuarios:
                archivo_usuarios.write(f"{new_user.id},{new_user.nombre},{new_user.contrasenia}\n")
            usuarios.append(new_user)
            mostrar_mensaje("Operación exitosa: Usuario registrado")
        else:
            mostrar_mensaje_err("Hubo un error")

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
                datos = usuario.strip().split(',')
                id = datos[0]
                nombre = datos[1]
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
        with open("C:/Archivos/Grupo4/Usuarios.txt", "r") as archivo_u:
            usuarios = archivo_u.readlines()

        usuarios_actualizados = []
        usuario_eliminado = False
        for usuario in usuarios:
            datos = usuario.strip().split(',')
            id = datos[0]
            if id != id_a_eliminar:
                usuarios_actualizados.append(usuario)
            else:
                usuario_eliminado = True

        if usuario_eliminado:
            with open("C:/Archivos/Grupo4/Usuarios.txt", "w") as archivo_u:
                archivo_u.writelines(usuarios_actualizados)
            mostrar_usuarios()
            mostrar_mensaje("Operación exitosa: Cliente Eliminado")
        else:
            mostrar_mensaje_err("Hubo un error")


    boton_eliminar_usuario = tk.Button(frame_u_eliminar, text="Eliminar usuario", command=eliminar_usuario)
    boton_eliminar_usuario.pack()
    return frame_u_eliminar

def modificar_usuario(frame):
    frame_u_modificar = tk.Frame(frame)

    def mostrar_usuarios():
        usuarios_disponibles.delete("1.0", tk.END)
        usuarios_disponibles.insert(tk.END, "Usuarios:\n")
        with open("C:/Archivos/Grupo4/Usuarios.txt", "r") as archivo_u:
            usuarios = archivo_u.readlines()
            for usuario in usuarios:
                datos = usuario.strip().split(',')
                id = datos[0]
                nombre = datos[1]
                usuarios_disponibles.insert(tk.END, f"ID: {id}, Nombre: {nombre}\n")

    boton_mostrar_usuarios = tk.Button(frame_u_modificar, text="Mostrar usuarios disponibles", command=mostrar_usuarios)
    boton_mostrar_usuarios.pack()
    usuarios_disponibles = tk.Text(frame_u_modificar, width=70, height=10)
    usuarios_disponibles.pack()
    
    label_u_modificar_nombre = tk.Label(frame_u_modificar, text="Nombre: (usuario)")
    label_u_modificar_contrasenia = tk.Label(frame_u_modificar, text="Contraseña: ")
    entrada_u_modificar_nombre = tk.Entry(frame_u_modificar)
    entrada_u_modificar_contrasenia = tk.Entry(frame_u_modificar)
    label_u_modificar_id = tk.Label(frame_u_modificar, text="ID del usuario a modificar:")
    entrada_u_modificar_id = tk.Entry(frame_u_modificar)

    label_u_modificar_nombre.pack()
    entrada_u_modificar_nombre.pack()
    label_u_modificar_contrasenia.pack()
    entrada_u_modificar_contrasenia.pack()
    label_u_modificar_id.pack()
    entrada_u_modificar_id.pack()

    def modificar_user():
        id_a_modificar = entrada_u_modificar_id.get()
        name = entrada_u_modificar_nombre.get()
        password = entrada_u_modificar_contrasenia.get()

        with open("C:/Archivos/Grupo4/Usuarios.txt", "r") as archivo_usuarios:
            usuarios = archivo_usuarios.readlines()

        usuarios_actualizados = []

        for usuario in usuarios:
            datos = usuario.strip().split(',')
            id = datos[0]
            if id == id_a_modificar:
                if name:
                    datos[1] = name
                if password:
                    datos[2] = password
                usuario_actualizado = ",".join(datos)
                usuarios_actualizados.append(usuario_actualizado)
            else:
                usuarios_actualizados.append(usuario)

        with open("C:/Archivos/Grupo4/Usuarios.txt", "w") as archivo_usuarios:
            archivo_usuarios.writelines("\n".join(usuarios_actualizados))
            archivo_usuarios.write("")
            mostrar_mensaje("Operación exitosa: Usuario modificado")

        mostrar_usuarios()

    boton_modificar_usuario = tk.Button(frame_u_modificar, text="Modificar usuario", command=modificar_user)
    boton_modificar_usuario.pack()

    return frame_u_modificar