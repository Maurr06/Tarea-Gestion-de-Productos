def AñadirProducto():
    nombre = input('Ingrese nombre: ')
    # Validar nombre
    while not nombre.isalpha():
        nombre = input('Ingrese nombre: ')
    
    # Validar PRECIO y convertir a float
    valido = False
    while valido == False:
        precio = input('Ingrese precio: ')
        try:
            precio = float(precio)
            if precio >= 0:
                valido = True # Sale del bucle solo si es valido
        except:
            print("Ingrese valor valido.") # Vuelve a pedir y validar, mediante el bucle while.

    # Validar CANTIDAD y convertir a entero
    valido = False
    while valido == False:
        cantidad = input('Ingrese cantidad: ')

        try:
            cantidad = int(cantidad)
            if cantidad >= 0:
                valido = True 
        except:
            print("Ingrese valor valido.") 
    
    dicc = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(dicc)

        
def VerProductos():
    for i in range(len(productos)):
        print(f"Producto Nº{i+1}")
        for llave in productos[i].keys():
            print(f"|\t{llave}: {productos[i][llave]}")

def ActualizarProducto():
    valido = False
    while valido == False:
        indice_producto = input('Ingrese numero de producto a actualizar: ')

        try:
            indice_producto = int(indice_producto)-1
            if indice_producto in range(len(productos)): # Si existe en productos
                valido = True 
        except:
            print("Ingrese valor valido.") 
        
    valido = False
    while valido == False:
        campo = input("Ingrese el campo a actualizar: ")
        if campo in productos[indice_producto].keys():
            valido = True
            productos[indice_producto][campo] = input('Ingrese valor a asignar: ')
        else:
            print('Campo invalido.')
    

def EliminarProducto():
    producto = input("Ingrese el nombre del producto a eliminar: ")
    encontrado = False
    for i in range(len(productos)):
        if productos[i]['nombre'] == producto:  # Compara con el nombre del producto.
            productos.pop(i)
            print(f"Producto \"{producto}\" eliminado.")
            encontrado = True
            break  # Sale del bucle después de eliminar el producto
    if not encontrado:
        print("El nombre de producto introducido no existe.")

def GuardarDatos():
    try:
        documento = open('productos.txt', 'w')
        for i in range(len(productos)):

            for llave in productos[i].keys():
                documento.write(f"{llave}: {productos[i][llave]}")
                if llave != 'cantidad':
                    documento.write(', ')

            documento.write('\n')
        documento.close()
    except:
        print("Error al abrir el documento productos.txt, revise si existe y si esta bien escrito.")

def CargarDatos():
    productos.clear()
    documento = open('productos.txt', 'r')
    
    for linea in documento.readlines():
        # Extraccion de informacion a partir de string
        partes = linea.split(', ')
        if len(partes) == 3:
            nombre = partes[0][8:]
            precio = float(partes[1][8:])
            cantidad = (partes[2][10:])
            
        # Carga en diccionario y lista
        dicc = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
        productos.append(dicc)
    documento.close()   



# Programa principal
productos = []
continuar = True
print("PROGRAMA DE GESTION DE PRODUCTOS.")

while continuar == True:
    print("\n1. Añadir producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Guardar datos")
    print("6. Cargar datos")
    print("7. Finalizar")
    opcion = input("Ingrese una opcion (1 al 7): ")

    if opcion.isdigit() and (1 <= int(opcion) <= 7): # Validacion de opcion
        match int(opcion):
            case 1:
                AñadirProducto() 
            case 2: 
                VerProductos() 
            case 3: 
                ActualizarProducto() 
            case 4: 
                EliminarProducto() 
            case 5: 
                GuardarDatos() 
            case 6: 
                CargarDatos()
            case 7: 
                print("Saliendo")
                continuar = False 
    else:
        print("Ingrese un valor valido.")