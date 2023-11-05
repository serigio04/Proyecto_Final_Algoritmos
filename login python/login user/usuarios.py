class Usuario:  

    numUsuarios = 0  
    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra
        self.conectado = False
        self.intentos = 9

        Usuario.numUsuarios += 1  
    def conectar(self):
        myContra = input("Ingrese su contraseña: ")  
        if myContra == self.contra:
            print("Se ha conectado con éxito")
            self.conectado = True
        else:
            print("Contraseña incorrecta, inténtelo de nuevo")
            self.intentos -= 1
            print("Intentos restantes:", self.intentos)         

def desconectar(self):
    if self.conectado:
        print("Se cerró la sesión con éxito")
        self.conectado = False
    else:
        print("Error, no se pudo iniciar con éxito")

def __str__(self):
    if self.conectado:
        conect = "conectado"
    else:
        conect = "desconectado"
    return f"mi nombre de usuario es {self.nombre} y estoy {conect}"

user1 = Usuario (input("ingrese un nombre: "), input ("ingrese su contraseña:"))
print(user1)