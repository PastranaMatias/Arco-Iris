from producto import Producto
from gestorproductos import GestorProductos
from interfaces.imostrable import IMostrable

def pedir_precio():
    while True:
        entrada = input("Ingrese precio: ")
        if not entrada.strip():
            print("El precio no puede estar vacío.")
            continue
        try:
            precio = float(entrada)
            if precio <= 0:
                print("El precio debe ser mayor a 0.")
                continue
            return precio
        except ValueError:
            print("Debe ingresar un número válido.")

def pedir_stock():
    while True:
        entrada = input("Ingrese stock inicial: ")
        if not entrada.strip():
            print("El stock no puede estar vacío.")
            continue
        try:
            stock = int(entrada)
            if stock < 0:
                print("El stock no puede ser negativo.")
                continue
            return stock
        except ValueError:
            print("Debe ingresar un número entero válido.")

def menu():
    productos = []

    while True:
        print("\n=== Sistema Arcoiris ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese nombre: ").strip()
            marca = input("Ingrese marca: ").strip()
            precio = pedir_precio()
            stock = pedir_stock()

            # Color opcional
            color = input("Ingrese color (dejar vacío si no aplica): ").strip()
            if not color:
                color = None

            try:
                nuevo = Producto(nombre, marca, precio, stock, color)
                productos.append(nuevo)
                nuevo.mostrar_confirmacion()
            except ValueError as e:
                print(e)

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
