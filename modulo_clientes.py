import tkinter as tk
class Cliente():
    def __init__(self, id, nombre, direccion, telefono, nit):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.nit = nit
clientes = []
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
            clientes.append({"Código": codigo, "Nombre": nombre, "Dirección": direccion, "Teléfono": telefono, "NIT": nit})
            # Puedes guardar los datos en un archivo o base de datos aquí si es necesario.

    boton_registrar_c = tk.Button(frame_c_agregar, text="Registrar Cliente", command=registrar_cliente)
    boton_registrar_c.pack()

    return frame_c_agregar

def eliminar_cliente(frame):
    frame_c_eliminar = tk.Frame(frame)
    label_cliente_eliminar = tk.Label(frame_c_eliminar, text="Selecciona un cliente:")
    lista_clientes_eliminar = tk.Listbox(frame_c_eliminar)
    
    for cliente in clientes:
        lista_clientes_eliminar.insert(tk.END, cliente["Código"])
    
    def eliminar_seleccionado():
        cliente_seleccionado = lista_clientes_eliminar.get(tk.ACTIVE)
        if cliente_seleccionado:
            for cliente in clientes:
                if cliente["Código"] == cliente_seleccionado:
                    clientes.remove(cliente)
                    break

    label_cliente_eliminar.pack()
    lista_clientes_eliminar.pack()
    
    boton_eliminar_seleccionado = tk.Button(frame_c_eliminar, text="Eliminar Cliente", command=eliminar_seleccionado)
    boton_eliminar_seleccionado.pack()

    return frame_c_eliminar

# Función para modificar un cliente en el módulo de clientes
def modificar_cliente(frame):
    frame_c_modificar = tk.Frame(frame)
    label_cliente_modificar = tk.Label(frame_c_modificar, text="Selecciona un cliente:")
    lista_clientes_modificar = tk.Listbox(frame_c_modificar)
    
    for cliente in clientes:
        lista_clientes_modificar.insert(tk.END, cliente["Código"])
    
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
            if cliente["Código"] == cliente_seleccionado:
                cliente["Código"] = nuevo_codigo
                cliente["Nombre"] = nuevo_nombre
                cliente["Dirección"] = nueva_direccion
                cliente["Teléfono"] = nuevo_telefono
                cliente["NIT"] = nuevo_nit
                break

    boton_modificar_seleccionado = tk.Button(frame_c_modificar, text="Modificar Cliente", command=modificar_seleccionado)
    boton_modificar_seleccionado.pack()

    return frame_c_modificar
