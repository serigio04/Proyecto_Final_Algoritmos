import tkinter as tk

class Cliente():
    def __init__(self, codigo, nombre, direccion, telefono, nit):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.nit = nit

clientes = []

# Función para mostrar un mensaje de operación exitosa
def mostrar_mensaje_exitoso(mensaje):
    exito_label = tk.Label(text=mensaje, fg="green")
    exito_label.pack()

# Función para cargar los clientes desde un archivo
def cargar_clientes_desde_archivo():
    try:
        with open("Clientes.txt", 'r') as archivo_clientes:
            for linea in archivo_clientes:
                codigo, nombre, direccion, telefono, nit = linea.strip().split(",")
                clientes.append(Cliente(codigo, nombre, direccion, telefono, nit))
    except Exception as e:
        mostrar_mensaje_exitoso(f"Error al cargar desde el archivo: {e}")

# Función para guardar los clientes en un archivo
def guardar_clientes_en_archivo():
    try:
        with open("Clientes.txt", 'w') as archivo_clientes:
            for cliente in clientes:
                archivo_clientes.write(f"{cliente.codigo},{cliente.nombre},{cliente.direccion},{cliente.telefono},{cliente.nit}\n")
        mostrar_mensaje_exitoso("Operación exitosa: Datos de clientes guardados.")
    except Exception as e:
        mostrar_mensaje_exitoso(f"Error al guardar en el archivo: {e}")

# Función para agregar un cliente
def agregar_cliente(frame):
    frame_c_agregar = tk.Frame(frame)

    label_codigo = tk.Label(frame_c_agregar, text="Código del Cliente:")
    entry_codigo = tk.Entry(frame_c_agregar)
    label_nombre = tk.Label(frame_c_agregar, text="Nombre del Cliente:")
    entry_nombre = tk.Entry(frame_c_agregar)
    label_direccion = tk.Label(frame_c_agregar, text="Dirección del Cliente:")
    entry_direccion = tk.Entry(frame_c_agregar)
    label_telefono = tk.Label(frame_c_agregar, text="Teléfono del Cliente:")
    entry_telefono = tk.Entry(frame_c_agregar)
    label_nit = tk.Label(frame_c_agregar, text="NIT del Cliente:")
    entry_nit = tk.Entry(frame_c_agregar)

    label_codigo.pack()
    entry_codigo.pack()
    label_nombre.pack()
    entry_nombre.pack()
    label_direccion.pack()
    entry_direccion.pack()
    label_telefono.pack()
    entry_telefono.pack()
    label_nit.pack()
    entry_nit.pack()

    def registrar_cliente():
        codigo = entry_codigo.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        nit = entry_nit.get()

        if codigo and nombre:
            clientes.append(Cliente(codigo, nombre, direccion, telefono, nit))
            guardar_clientes_en_archivo()
            mostrar_mensaje_exitoso("Operación exitosa: Cliente registrado.")

    boton_registrar_c = tk.Button(frame_c_agregar, text="Registrar Cliente", command=registrar_cliente)
    boton_registrar_c.pack()

    return frame_c_agregar

# Función para eliminar un cliente
def eliminar_cliente(frame, lista_clientes_eliminar):
    frame_c_eliminar = tk.Frame(frame)
    label_cliente_eliminar = tk.Label(frame_c_eliminar, text="Selecciona un cliente:")
    lista_clientes_eliminar = tk.Listbox(frame_c_eliminar)

    for cliente in clientes:
        lista_clientes_eliminar.insert(tk.END, cliente.codigo)

    def eliminar_seleccionado():
        cliente_seleccionado = lista_clientes_eliminar.get(tk.ACTIVE)
        if cliente_seleccionado:
            for cliente in clientes:
                if cliente.codigo == cliente_seleccionado:
                    clientes.remove(cliente)
                    guardar_clientes_en_archivo()
                    actualizar_lista_clientes(lista_clientes_eliminar)  # Actualiza la lista
                    mostrar_mensaje_exitoso("Operación exitosa: Cliente eliminado.")
                    break

    label_cliente_eliminar.pack()
    lista_clientes_eliminar.pack()

    boton_eliminar_seleccionado = tk.Button(frame_c_eliminar, text="Eliminar Cliente", command=eliminar_seleccionado)
    boton_eliminar_seleccionado.pack()

    return frame_c_eliminar

# Función para modificar un cliente
def modificar_cliente(frame, lista_clientes_modificar):
    frame_c_modificar = tk.Frame(frame)
    label_cliente_modificar = tk.Label(frame_c_modificar, text="Selecciona un cliente:")
    lista_clientes_modificar = tk.Listbox(frame_c_modificar)

    for cliente in clientes:
        lista_clientes_modificar.insert(tk.END, cliente.codigo)

    label_cliente_modificar.pack()
    lista_clientes_modificar.pack()

    label_nuevo_codigo = tk.Label(frame_c_modificar, text="Nuevo Código:")
    entry_nuevo_codigo = tk.Entry(frame_c_modificar)
    label_nuevo_nombre = tk.Label(frame_c_modificar, text="Nuevo Nombre:")
    entry_nuevo_nombre = tk.Entry(frame_c_modificar)
    label_nueva_direccion = tk.Label(frame_c_modificar, text="Nueva Dirección:")
    entry_nueva_direccion = tk.Entry(frame_c_modificar)
    label_nuevo_telefono = tk.Label(frame_c_modificar, text="Nuevo Teléfono:")
    entry_nuevo_telefono = tk.Entry(frame_c_modificar)
    label_nuevo_nit = tk.Label(frame_c_modificar, text="Nuevo NIT:")
    entry_nuevo_nit = tk.Entry(frame_c_modificar)

    label_nuevo_codigo.pack()
    entry_nuevo_codigo.pack()
    label_nuevo_nombre.pack()
    entry_nuevo_nombre.pack()
    label_nueva_direccion.pack()
    entry_nueva_direccion.pack()
    label_nuevo_telefono.pack()
    entry_nuevo_telefono.pack()
    label_nuevo_nit.pack()
    entry_nuevo_nit.pack()

    def modificar_seleccionado():
        cliente_seleccionado = lista_clientes_modificar.get(tk.ACTIVE)
        nuevo_codigo = entry_nuevo_codigo.get()
        nuevo_nombre = entry_nuevo_nombre.get()
        nueva_direccion = entry_nueva_direccion.get()
        nuevo_telefono = entry_nuevo_telefono.get()
        nuevo_nit = entry_nuevo_nit.get()

        for cliente in clientes:
            if cliente.codigo == cliente_seleccionado:
                cliente.codigo = nuevo_codigo
                cliente.nombre = nuevo_nombre
                cliente.direccion = nueva_direccion
                cliente.telefono = nuevo_telefono
                cliente.nit = nuevo_nit
                guardar_clientes_en_archivo()
                cargar_clientes_desde_archivo()
                actualizar_lista_clientes(lista_clientes_modificar)  # Actualiza la lista
                mostrar_mensaje_exitoso("Operación exitosa: Cliente modificado.")
                break

    boton_modificar_seleccionado = tk.Button(frame_c_modificar, text="Modificar Cliente", command=modificar_seleccionado)
    boton_modificar_seleccionado.pack()

    return frame_c_modificar

# Función para actualizar la lista de clientes en el frame
def actualizar_lista_clientes(lista):
    lista.delete(0, tk.END)
    for cliente in clientes:
        lista.insert(tk.END, cliente.codigo)