print("Departamento de confección")
print("1.Ingresar producto ")
print("2.Mostrar inventario en fábrica ")
print("0. SALIR")
opcion = 1
listaProductos = []

while opcion != 0 :
    opcion = int(input("Digita una opción"))
    if opcion == 1:
        producto = input("Digita el producto que ingresa a fabricación")
        #Agregar un porducto a la lista de prdcuto
        listaProductos.append(producto)
    elif opcion == 2:
        print(listaProductos)
    elif opcion > 3 or opcion < 0:
        print("Opcón no valida")
    else:
        print("Se salió")
        
print("Fin del programa")
    