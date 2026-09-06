from producto import Producto

def menu():
    productos = []

    while True:
        print("\n=== Sistema Arcoiris ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            marca = input("Ingrese marca: ")
            precio = float(input("Ingrese precio: "))
            stock = int(input("Ingrese stock inicial: "))

            nuevo = Producto(nombre, marca, precio, stock)
            productos.append(nuevo)
            nuevo.mostrar_confirmacion()

        elif opcion == "2":
            if productos:
                print("\n=== Lista de productos ===")
                for p in productos:
                    p.mostrar_confirmacion()
            else:
                print("No hay productos registrados todavía.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
