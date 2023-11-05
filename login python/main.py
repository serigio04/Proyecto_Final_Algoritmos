from tkinter import *
from tkinter import ttk as ttk

# Ventana principal
root = Tk()
root.title("Login Usuario")

# MainFrame
mainFrame = Frame(root)
mainFrame.pack()
mainFrame.config(width=400, height=320, bg="white")

# Textos y títulos
titulo = Label(mainFrame, text="Login  ", font=("Arial", 25))
titulo.grid(column=0, row=0, padx=10, pady=10)

nombreLabel = Label(mainFrame, text="Nombre: ")
nombreLabel.grid(column=0, row=1)
passLabel = Label(mainFrame, text="Contraseña: ")
passLabel.grid(column=0, row=2)

# Entradas de texto
nombreUsuario = StringVar()
nombreUsuario.set("lucas")
nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
nombreEntry.grid(column=1, row=1)

contraUsuario = StringVar()
contraUsuario.set("1234")
contraEntry = Entry(mainFrame, textvariable=contraUsuario, show="*")
contraEntry.grid(column=1, row=2)

# Botones
iniciarSesionButton = ttk.Button(mainFrame, text="Iniciar Sesión")
iniciarSesionButton.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)

registrarButton = ttk.Button(mainFrame, text="Registrar")
registrarButton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

root.mainloop()
