from sre_parse import CATEGORIES
import tkinter as tk


class Producto():
    def __init__(self, codigo, nombre, descripcion, precio, cantidad, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        
productos=[]
            
def mostrar_mensaje_exitoso(mensaje):
    exito_label = tk.Label(text=mensaje, fg="green")
    exito_label.pack()

            
def guardar_productos_en_archivo():
    try:
        with open(r'C:\Archivos\Grupo4\Inventario.txt', 'a') as archivo_producto:
            for producto in productos:
                archivo_producto.write(f"{producto.codigo},{producto.nombre},{producto.descripcion},{producto.precio},{producto.cantidad},{producto.categoria}\n")
        mostrar_mensaje_exitoso("Operación exitosa: Datos de producto guardados.")
    except Exception as e:
        mostrar_mensaje_exitoso(f"Error al guardar en el archivo: {e}")
            
        
def agregar_producto(frame):
    frame_p_agregar = tk.Frame(frame)
    
    label_codigo = tk.Label(frame_p_agregar, text="Código del Producto:")
    entry_codigo = tk.Entry(frame_p_agregar)
    label_nombre = tk.Label(frame_p_agregar, text="Nombre del Producto:")
    entry_nombre = tk.Entry(frame_p_agregar)
    label_Descripcion = tk.Label(frame_p_agregar, text="Descripción del Producto:")
    entry_Descripcion = tk.Entry(frame_p_agregar)
    label_precio = tk.Label(frame_p_agregar, text="Precio del Producto:")
    entry_precio = tk.Entry(frame_p_agregar)
    label_cantidad = tk.Label(frame_p_agregar, text="Ingrese cantidad del Producto:")
    entry_cantidad = tk.Entry(frame_p_agregar)
    label_Categoria = tk.Label(frame_p_agregar, text="Ingrese la categoría del Producto:")
    entry_Categoria = tk.Entry(frame_p_agregar)

    label_codigo.pack()
    entry_codigo.pack()
    label_nombre.pack()
    entry_nombre.pack()
    label_Descripcion.pack()
    entry_Descripcion.pack()
    label_precio.pack()
    entry_precio.pack()
    label_cantidad.pack()
    entry_cantidad.pack()
    label_Categoria.pack()
    entry_Categoria.pack()
    
    
    def registrar_producto():
        codigo = entry_codigo.get()
        nombre = entry_nombre.get()
        descripcion = entry_Descripcion.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        categoría = entry_Categoria.get()
        
        
        if codigo and nombre :
          nuevo_producto = Producto(codigo, nombre, descripcion, precio, cantidad, categoría)
          productos.append(nuevo_producto)
          guardar_productos_en_archivo()
          mostrar_mensaje_exitoso("Operación exitosa: Producto agregado.")
            
    boton_agregar_p = tk.Button(frame_p_agregar, text="Agregar Producto", command=registrar_producto)
    boton_agregar_p.pack()

    return frame_p_agregar


    

  
def modificar_producto(frame):
    frame_p_modificar = tk.Frame(frame)
    
    label_codigo = tk.Label(frame_p_modificar, text="Código del Producto:")
    entry_codigo = tk.Entry(frame_p_modificar)
    label_nombre = tk.Label(frame_p_modificar, text="Nombre del Producto:")
    entry_nombre = tk.Entry(frame_p_modificar)
    label_Descripcion = tk.Label(frame_p_modificar, text="Descripción del Producto:")
    entry_Descripcion = tk.Entry(frame_p_modificar)
    label_precio = tk.Label(frame_p_modificar, text="Precio del Producto:")
    entry_precio = tk.Entry(frame_p_modificar)
    label_cantidad = tk.Label(frame_p_modificar, text="Ingrese cantidad del Producto:")
    entry_cantidad = tk.Entry(frame_p_modificar)
    label_Categoria = tk.Label(frame_p_modificar, text="Ingrese la categoría del Producto:")
    entry_Categoria = tk.Entry(frame_p_modificar)
    
    
    label_codigo.pack()
    entry_codigo.pack()
    label_nombre.pack()
    entry_nombre.pack()
    label_Descripcion.pack()
    entry_Descripcion.pack()
    label_precio.pack()
    entry_precio.pack()
    label_cantidad.pack()
    entry_cantidad.pack()
    label_Categoria.pack()
    entry_Categoria.pack()
    

    
    def mostrar_productos():
        productos_disponibles.delete("1.0", tk.END)
        productos_disponibles.insert(tk.END, "Usuarios:\n")
        with open("C:\Archivos\Grupo4\Inventario.txt", "r") as archivo_p:
            productos = archivo_p.readlines()
            for productos in productos:
                id, nombre = productos.strip().split(',')
                productos_disponibles.insert(tk.END, f"ID: {id}, Nombre: {nombre}\n")
                
    boton_mostrar_productos = tk.Button(frame_p_modificar, text="Mostrar productos disponibles", command=mostrar_productos)
    boton_mostrar_productos.pack()
    productos_disponibles = tk.Text(frame_p_modificar, width=70, height=10)
    productos_disponibles.pack()
    
    boton_agregar_p = tk.Button(frame_p_modificar, text="Agregar Producto", command=modificar_producto)
    boton_agregar_p.pack()
    
    
    
    return frame_p_modificar

def consultar_producto(frame):
    frame_p_consultar= tk.frame(frame)
