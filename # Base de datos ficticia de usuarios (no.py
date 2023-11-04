# Base de datos ficticia de usuarios (nombre de usuario y contraseña)
database = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2',
    'usuario3': 'contraseña3'
}

# Función para el inicio de sesión
def login():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if username in database and database[username] == password:
        print("Inicio de sesión exitoso. Bienvenido, " + username + "!")
        # Puedes agregar más acciones aquí después del inicio de sesión exitoso.
    else:
        print("Credenciales incorrectas. Inténtelo de nuevo.")

# Función para la salida de sistema
def logout():
    print("Sesión cerrada. ¡Hasta luego!")

# Menú principal
while True:
    print("\n1. Iniciar sesión")
    print("2. Salir del sistema")
    choice = input("Seleccione una opción: ")

    if choice == '1':
        login()
    elif choice == '2':
        logout()
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")