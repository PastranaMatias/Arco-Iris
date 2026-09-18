from producto import Producto
from gestorproductos import GestorProductos

def pedir_precio():
    while True:
        entrada = input("Ingrese precio de costo: ").strip()
        if not entrada:
            print("❌ El precio no puede estar vacío.")
            continue
        try:
            precio = float(entrada)
            if precio <= 0:
                print("❌ El precio debe ser mayor a 0.")
                continue
            return precio
        except ValueError:
            print("❌ Debe ingresar un número válido.")

def pedir_stock():
    while True:
        entrada = input("Ingrese stock inicial: ").strip()
        if not entrada:
            print("❌ El stock no puede estar vacío.")
            continue
        try:
            stock = int(entrada)
            if stock < 0:
                print("❌ El stock no puede ser negativo.")
                continue
            return stock
        except ValueError:
            print("❌ Debe ingresar un número entero válido.")

def menu():
    gestor = GestorProductos()

    while True:
        print("\n=== Sistema Arcoiris ===")
        print("1. Registrar producto")
        print("2. Mostrar lista de precios y stock")
        print("3. Sumar stock a producto existente")
        print("4. Descontar stock por venta/rotura")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese nombre: ").strip()
            marca = input("Ingrese marca: ").strip()
            color = input("Ingrese color (opcional): ").strip() or None

            try:
                precio_costo = pedir_precio()
                stock = pedir_stock()
                nuevo = Producto(nombre, marca, precio_costo, stock, color)
                gestor.agregar_producto(nuevo)
            except ValueError as e:
                print(e)

        elif opcion == "2":
            gestor.mostrar()

        elif opcion == "3":
            nombre = input("Ingrese nombre del producto: ").strip()
            marca = input("Ingrese marca del producto: ").strip()
            color = input("Ingrese color del producto (opcional): ").strip() or None
            try:
                cantidad = int(input("Ingrese cantidad a sumar: "))
                gestor.modificar_stock(nombre, marca, color, cantidad)
            except ValueError:
                print("❌ Debe ingresar un número entero válido.")

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto: ").strip()
            marca = input("Ingrese marca del producto: ").strip()
            color = input("Ingrese color del producto (opcional): ").strip() or None
            try:
                cantidad = int(input("Ingrese cantidad a descontar: "))
                gestor.modificar_stock(nombre, marca, color, -cantidad)
            except ValueError:
                print("❌ Debe ingresar un número entero válido.")

        elif opcion == "5":
            nombre = input("Ingrese nombre del producto: ").strip()
            marca = input("Ingrese marca del producto: ").strip()
            color = input("Ingrese color del producto (opcional): ").strip() or None
            gestor.eliminar_producto(nombre, marca, color)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
