from producto import Producto
from gestorproductos import GestorProductos
from interfaces.imostrable import IMostrable
from descuento import Descuento
from ticket import Ticket
import os #para limpiar pantalla


def limpiarPantalla():
    os.system("cls")

gestP=GestorProductos() #creo al gestor de productos /para verificar
produc=Producto(1,"pintura","Grre",120,5,"rojo") #productos de prueba
prod=Producto(2,"fresstal","Blue",120,7,"Azul")
gestP.agregarProducto(produc)
gestP.agregarProducto(prod)
gestP.verificarStock(prod)

def genTi(): 
    item =[]

    while True:  
        limpiarPantalla()
        print(" === Cobro ===")

        while True:
            try:
                id=int(input("ing id del producto: "))
                producto=gestP.buscarProducto(id)

                if producto is None:
                   print("No existe un producto con ese ID")
                   continue
                break

            except ValueError:
              print ("Debe ingresar un ID Valido")

        if gestP.verificarStock(producto):
            while True:
                try:
                    cant=int(input("ing cantidad: "))

                    if cant<=0: 
                        print("La cantidad debe ser mayor a 0")
                        continue
                    try:
                        producto.actualizar_stock(-cant)
                        break #stock actualizado exitosamente
                    except ValueError as e:
                        print(e)
                    
                except ValueError:
                    print("Debe ingresar un numero")

            item.append((id,cant)) 
            print(f"agregado: {producto.nombre} x{cant}")
            
        else:
            print("Necesita renovar el stock")                          
            print("El producto no fue agregado")

        while True:
            try:
                print("Desea agregar otro producto, precione:")
                print("1- Si")
                print("0- No, ir a forma de pago")
                re=int(input())

                if re==0:
                    break
                elif re==1 : 
                    break
                else:
                    print("Dato erroneo") 

            except ValueError():
                print ("Opcion Invalida")

        if re==0: 
            break

    limpiarPantalla()
    ticke=gestP.generarTicket(item) #genero ticket
    subtotal=ticke.calTotal()  #guarto el total sin descuento

    while True:
        try:
            print("Formas de Pago:")   
            print("1- Efectivo")
            print ("2- Tarjeta")
            forma=int(input())
            
            if forma==1:
                desc=Descuento("Efectivo",10) 
                break
            elif forma==2:
                desc=Descuento("Credito",15)
                break
            else: #desc=None
                print("Opcion invalida")
        except ValueError:
            print("Elija una de esas opciones")

    if desc:
        totalFinal=desc.aplicar(subtotal)

    else: totalFinal=subtotal
    
    limpiarPantalla()
    ticke.impriTiket()
    print(f"Precio: ${subtotal}")
    if desc.tipo=="efectivo":
        print(f"Descuento:{desc.porcentaje}%")
    elif desc.tipo=="credito":
        print(f"Recargo:{desc.porcentaje}%")
    print(f"Precio Final: ${totalFinal}")

    print("Enter para volver al menu")
    input()


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
        limpiarPantalla() # limpio lo q estaba arriba de la terminal
        print("\n=== Sistema Arcoiris ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Cobrar Productos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id=int(input("ingrese ID"))
            nombre = input("Ingrese nombre: ").strip()
            marca = input("Ingrese marca: ").strip()
            precio = pedir_precio()
            stock = pedir_stock()

            # Color opcional
            color = input("Ingrese color (dejar vacío si no aplica): ").strip()
            if not color:
                color = None

            try:
                nuevo = Producto(id,nombre, marca, precio, stock, color)
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

        elif opcion=="3":
            genTi()


        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
