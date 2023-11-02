import tkinter as tk
from modulo_usuarios import agregar_usuario, eliminar_usuario, modificar_usuario

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
    #otrosFrames.pack_forget()

def abrir_clientes():
    pass

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
def volver_menu():
    frame_usuarios.pack_forget()
    boton_usuarios.pack()
    boton_clientes.pack()
    boton_productos.pack()
    boton_categorias.pack()
    boton_facturacion.pack()

boton_volver = tk.Button(frame_usuarios, text="Menú principal", command=volver_menu)
label_usuarios = tk.Label(frame_usuarios, text="¿Qué quieres hacer?")
boton_u_agregar = tk.Button(frame_usuarios, text="Agregar usuario", command=agregar_usuario)
boton_u_eliminar = tk.Button(frame_usuarios, text="Eliminar usuario", command=eliminar_usuario)
boton_u_modificar = tk.Button(frame_usuarios, text="Modificar usuario", command=modificar_usuario)

boton_volver.pack()
label_usuarios.pack()
boton_u_agregar.pack()
boton_u_eliminar.pack()
boton_u_modificar.pack()


app.mainloop()