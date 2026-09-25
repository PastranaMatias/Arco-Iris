from producto import Producto
from gestorproductos import GestorProductos
from interfaces.imostrable import IMostrable
from descuento import Descuento
from ticket import Ticket
import os  # para limpiar pantalla


def limpiarPantalla():
    os.system("cls")


gestP = GestorProductos()  # creo al gestor de productos


def inicializar_productos():
    """Carga productos de prueba al iniciar el sistema"""
    produc = Producto(1, "pintura", "Grre", 120, 5, "rojo")
    prod = Producto(2, "fresstal", "Blue", 120, 7, "Azul")
    gestP.agregarProducto(produc)
    gestP.agregarProducto(prod)


def pedir_precio():
    while True:
        entrada = input("Ingrese precio: ")
        if not entrada.strip():
            print(" El precio no puede estar vacío.")
            continue
        try:
            precio = float(entrada)
            if precio <= 0:
                print(" El precio debe ser mayor a 0.")
                continue
            return precio
        except ValueError:
            print(" Debe ingresar un número válido.")


def pedir_stock():
    while True:
        entrada = input("Ingrese stock inicial: ")
        if not entrada.strip():
            print(" El stock no puede estar vacío.")
            continue
        try:
            stock = int(entrada)
            if stock < 0:
                print(" El stock no puede ser negativo.")
                continue
            return stock
        except ValueError:
            print(" Debe ingresar un número entero válido.")


def genTi():
    item = []

    while True:
        limpiarPantalla()
        print(" === Cobro ===")

        while True:
            try:
                entrada = input("ing id del producto: ").strip()
                if not entrada:
                    print(" El ID no puede estar vacío.")
                    continue

                id = int(entrada)
                producto = gestP.buscarProducto(id)

                if producto is None:
                    print("No existe un producto con ese ID")
                    continue
                break

            except ValueError:
                print("Debe ingresar un ID válido")

        if gestP.verificarStock(producto):
            while True:
                try:
                    cant = int(input("ing cantidad: "))

                    if cant <= 0:
                        print("La cantidad debe ser mayor a 0")
                        continue
                    try:
                        producto.actualizar_stock(-cant)
                        break
                    except ValueError as e:
                        print(e)

                except ValueError:
                    print("Debe ingresar un número")

            item.append((id, cant))
            print(f"agregado: {producto.nombre} x{cant}")

        else:
            print("Necesita renovar el stock")
            print("El producto no fue agregado")

        while True:
            try:
                print("Desea agregar otro producto, precione:")
                print("1- Si")
                print("0- No, ir a forma de pago")
                re = int(input())

                if re == 0:
                    break
                elif re == 1:
                    break
                else:
                    print("Dato erróneo")

            except ValueError:
                print("Opción inválida")

        if re == 0:
            break

    limpiarPantalla()
    ticke = gestP.generarTicket(item)
    subtotal = ticke.calTotal()

    while True:
        try:
            print("Formas de Pago:")
            print("1- Efectivo")
            print("2- Tarjeta")
            forma = int(input())

            if forma == 1:
                desc = Descuento("Efectivo", 10)
                break
            elif forma == 2:
                desc = Descuento("Credito", 15)
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Elija una de esas opciones")

    if desc:
        totalFinal = desc.aplicar(subtotal)
    else:
        totalFinal = subtotal

    limpiarPantalla()
    ticke.impriTiket()
    print(f"Precio: ${subtotal}")
    if desc.tipo.lower() == "efectivo":
        print(f"Descuento: {desc.porcentaje}%")
    elif desc.tipo.lower() == "credito":
        print(f"Recargo: {desc.porcentaje}%")
    print(f"Precio Final: ${totalFinal}")

    print("Enter para volver al menú")
    input()


def menu():
    while True:
        limpiarPantalla()
        print("\n=== Sistema Arcoiris ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Cobrar Productos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                entrada = input("Ingrese ID: ").strip()
                if not entrada:
                    print(" El ID no puede estar vacío.")
                    continue
                try:
                    id = int(entrada)
                    break
                except ValueError:
                    print(" Debe ingresar un número válido.")

            nombre = input("Ingrese nombre: ").strip()
            marca = input("Ingrese marca: ").strip()
            precio = pedir_precio()
            stock = pedir_stock()

            color = input("Ingrese color (dejar vacío si no aplica): ").strip()
            if not color:
                color = None

            try:
                nuevo = Producto(id, nombre, marca, precio, stock, color)
                gestP.agregarProducto(nuevo)
                nuevo.mostrar_confirmacion()
                input("Enter para volver al menú")
            except ValueError as e:
                print(e)
                input("Enter para volver al menú")

        elif opcion == "2":
            if gestP.ListaProductos:
                print("\n=== Lista de productos ===")
                for p in gestP.ListaProductos:
                    print(f"ID: {p.id} | ", end="")  #  ahora se muestra el ID
                    p.mostrar_confirmacion()
            else:
                print("No hay productos registrados todavía.")

            input("Enter para volver al menú")

        elif opcion == "3":
            genTi()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    inicializar_productos()  #  se cargan los dos productos de prueba
    menu()

