from producto import Producto
from gestorproductos import GestorProductos
from descuento import Descuento
from pedido import Pedido
from ticket import Ticket
import os #para limpiar pantalla


def limpiarPantalla():
    os.system("cls")

gestP=GestorProductos() #creo al gestor de productos

def pedirProd():
    product=[]

    print("Ingre info del producto a pedir")
    id=input("ing id del producto")
    cant=input("ing cantidad")
    
    #product.append(pedido)
    print("Desea agregar otro producto" \
    "precione:")

    print("1- Si")
    print ("0- No, ir a forma de pago")
    
    ver=int(input())
    if ver==0:
        print ("a")
        #revisar !!!!
def genTi(): 
    item =[]

    while True:  
        print(" === Cobro ===")
        id=int(input("ing id del producto: "))
        cant=int(input("ing cantidad: "))

        item.append((id,cant))

        print("Desea agregar otro producto, precione:")
        print("1- Si")
        print("0- No, ir a forma de pago")
        re=int(input())

        if re==0:
            break
        elif re!=1 : print("Dato erroneo") #agregar un execion

    ticke=gestP.generarTicket(item) #genero ticket
    subtotal=ticke.calTotal()  #guarto el total sin descuento

    print("Formas de Pago:")   
    print("1- Efectivo")
    print ("2- Tarjeta")
    forma=int(input())

    if forma==1:
        desc=Descuento("Efectivo",10) 

    elif forma==2:
        desc=Descuento("Credito",15)
    
    else:desc=None

    if desc:
        totalFinal=desc.aplicar(subtotal)

    else: totalFinal=subtotal

    ticke.impriTiket()
    print(f"Precio: ${subtotal}")
    if desc.tipo=="efectivo":
        print(f"Descuento:{desc.porcentaje}%")
    elif desc.tipo=="credito":
        print(f"Recargo:{desc.porcentaje}%")
    print(f"Precio Final: ${totalFinal}")

    print("Enter para volver al menu")
    input()

    
produc=Producto(1,"pintura","Grre",120,"rojo",5)
prod=Producto(2,"pintura","Blue",120,"azul",7)
gestP.agregarProducto(produc)
gestP.agregarProducto(prod)
gestP.verificarStock(prod)
def menu():

    productos = []

    while True:
        limpiarPantalla()
        print("\n=== Sistema Arcoiris ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Cobrar Productos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion=="3":
            
            #produc=Producto(1,"pintura","Grre",120,"rojo",5)
            #prod=Producto(2,"pintura","Blue",120,"azul",7)
            #gestP.agregarProducto(produc)
            #gestP.agregarProducto(prod)
            #gestP.verificarStock(prod)
            genTi()


        elif opcion == "1":
            precio = int(input("Ingrese Id: "))
            nombre = input("Ingrese nombre: ")
            marca = input("Ingrese marca: ")
            precio = float(input("Ingrese precio: "))
            stock = int(input("Ingrese stock inicial: "))

            nuevo = Producto(id,nombre, marca, precio, stock)
            #productos.append(nuevo)
            #nuevo.mostrar_confirmacion()
            gestP.agregarProducto(nuevo) #agrego al productos al gestorP

        elif opcion == "2":
            if productos:
                print("\n=== Lista de productos ===")
                for p in productos:
                    p.mostrar_confirmacion()
            else:
                print("No hay productos registrados todavía.")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

#yo desde aca
