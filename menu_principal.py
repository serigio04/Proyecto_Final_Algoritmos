import tkinter as tk
from modulo_usuarios import agregar_usuario, eliminar_usuario, modificar_usuario
from modulo_clientes import agregar_cliente, eliminar_cliente, modificar_cliente

#pantalla del menú
app = tk.Tk()
app.title("Proyecto final Algoritmos")
app.geometry("900x600")

def abrir_usuarios():
    frame_usuarios.pack()
    boton_usuarios.pack_forget()
    boton_clientes.pack_forget()
    boton_productos.pack_forget()
    boton_categorias.pack_forget()
    boton_facturacion.pack_forget()
    boton_salir.pack_forget()

def abrir_clientes():
    frame_clientes.pack()
    boton_usuarios.pack_forget()
    boton_clientes.pack_forget()
    boton_productos.pack_forget()
    boton_categorias.pack_forget()
    boton_facturacion.pack_forget()
    boton_salir.pack_forget()


def abrir_productos():
    pass

def abrir_categorias():
    pass

def facturacion():
    pass

def salir():
    pass

boton_usuarios = tk.Button(app, text="USUARIOS", command=abrir_usuarios)
boton_usuarios.pack()
boton_clientes = tk.Button(app, text="CLIENTES", command=abrir_clientes)
boton_clientes.pack()
boton_productos = tk.Button(app, text="PRODUCTOS", command=abrir_productos)
boton_productos.pack()
boton_categorias = tk.Button(app, text="CATEGORIAS DE PRODUCTOS", command=abrir_categorias)
boton_categorias.pack()
boton_facturacion = tk.Button(app, text="FACTURACION", command=facturacion)
boton_facturacion.pack()
boton_salir = tk.Button(app, text="SALIR", command=salir)
boton_salir.pack()

#frame de usuarios
frame_usuarios = tk.Frame(app)
def volver_menu_u():
    frame_usuarios.pack_forget()
    boton_usuarios.pack()
    boton_clientes.pack()
    boton_productos.pack()
    boton_categorias.pack()
    boton_facturacion.pack()
    
def volver_menu_c():
    frame_clientes.pack_forget()
    boton_usuarios.pack()
    boton_clientes.pack()
    boton_productos.pack()
    boton_categorias.pack()
    boton_facturacion.pack()

boton_volver = tk.Button(frame_usuarios, text="Menú principal", command=volver_menu_u)
label_usuarios = tk.Label(frame_usuarios, text="¿Qué quieres hacer?")
boton_u_agregar = tk.Button(frame_usuarios, text="Registrar usuario", command=lambda: agregar_usuario(frame_usuarios).pack())
boton_u_eliminar = tk.Button(frame_usuarios, text="Eliminar usuario", command=lambda: eliminar_usuario(frame_usuarios).pack())
boton_u_modificar = tk.Button(frame_usuarios, text="Modificar usuario", command=lambda: modificar_usuario(frame_usuarios).pack())

boton_volver.pack()
label_usuarios.pack()
boton_u_agregar.pack()
boton_u_eliminar.pack()
boton_u_modificar.pack()

# frame clientes
frame_clientes = tk.Frame(app)


boton_volver_clientes = tk.Button(frame_clientes, text="Menú principal", command=volver_menu_c)
label_clientes = tk.Label(frame_clientes, text="¿Qué quieres hacer?")
boton_c_agregar = tk.Button(frame_clientes, text="Agregar Cliente", command=lambda: agregar_cliente(frame_clientes).pack())
boton_c_eliminar = tk.Button(frame_clientes, text="Eliminar Cliente", command=lambda: eliminar_cliente(frame_clientes).pack())
boton_c_modificar = tk.Button(frame_clientes, text="Modificar Cliente", command=lambda: modificar_cliente(frame_clientes).pack())

boton_volver_clientes.pack()
label_clientes.pack()
boton_c_agregar.pack()
boton_c_eliminar.pack()
boton_c_modificar.pack()

app.mainloop()