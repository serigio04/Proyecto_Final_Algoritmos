import tkinter as tk
from modulo_usuarios import agregar_usuario, eliminar_usuario, modificar_usuario

#pantalla del menú
app = tk.Tk()
app.title("Proyecto final Algoritmos")
app.geometry("900x600")

def abrir_usuarios():
    frame_usuarios.pack()
    #otrosFrames.pack_forget()

def abrir_clientes():
    pass

def abrir_productos():
    pass

def abrir_categorias_productos():
    pass

def facturacion():
    pass

def salir():
    pass

#frame de usuarios
frame_usuarios = tk.Frame(app)

def volver_menu():
    frame_usuarios.pack_forget()

boton_volver = tk.Button(frame_usuarios, text="Menú principal", command=volver_menu)

label_usuarios = tk.Label(frame_usuarios, text="¿Qué quieres hacer?")

boton_agregar = tk.Button(frame_usuarios, text="Agregar usuario", command=agregar_usuario)

boton_volver.pack()
label_usuarios.pack()
boton_agregar.pack()


app.mainloop()