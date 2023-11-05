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
            self.intentos -= 1
            if self.intentos > 0:
                print("Contraseña incorrecta, inténtelo de nuevo")
                print("Intentos restantes:", self.intentos)
                self.conectar()
            else:
                print("Error, no se pudo iniciar sesión.")
                print ("adios")

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
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"

user1 = Usuario(input("Ingrese un nombre: "), input("Ingrese su contraseña:"))
print(user1)

user1.conectar()
print(user1)

user1.desconectar()
print(user1)