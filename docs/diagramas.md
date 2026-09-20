# Diagramas del Proyecto Arco-Iris

## Diagrama de Clases
```mermaid
classDiagram
    class Producto {
        - id : int
        - nombre : string
        - marca : string
        - precio : float
        - stock : int
        - color : string
        + actualizar_stock(cantidad:int)
        + mostrar_confirmacion()
        + calcular_precio() : float
    }

    class GestorProductos {
        - ListaProductos : List<Producto>
        + agregarProducto(p:Producto)
        + aplicarDescuento(p:Producto, d:Descuento) : float
        + verificarStock(p:Producto) : bool
        + mostrarPreciosFinales()
        + generarTicket(items:List)
        + buscarProducto(id:int) : Producto
    }

    class Ticket {
        - items : List<(Producto,int)>
        + agregarP(pro:Producto, can:int)
        + calTotal() : float
        + impriTiket()
    }

    class Descuento {
        - tipo : string
        - porcentaje : int
        + aplicar(precio:float) : float
    }

    class Stock {
        - cantidadDisponible : int
        - alerta : bool
        + verifica() : bool
    }

    class Pedido {
        - IdPedido : int
        - fecha : date
        - estado : string
        - prodSoli : List<Producto>
        + generarPedido(listaProduc:List<Producto>)
        + actualizarEstado(nuevoEstado:string)
    }

    class Usuario {
        - nombre : string
        - dni : string
        - id : string
        + mostrar()
    }

    GestorProductos --> Producto
    GestorProductos --> Ticket
    GestorProductos --> Descuento
    GestorProductos --> Stock
    Pedido --> Producto
    Ticket --> Producto
    Usuario --> IMostrable


flowchart TD
    A[Inicio Cobro] --> B[Ingresar productos]
    B --> C[Generar Ticket]
    C --> D[Calcular subtotal]
    D --> E[Seleccionar forma de pago]
    E --> F{Efectivo o Crédito?}
    F -->|Efectivo| G[Aplicar descuento]
    F -->|Crédito| H[Aplicar recargo]
    G --> I[Mostrar ticket final]
    H --> I[Mostrar ticket final]
    I --> J[Fin]


sequenceDiagram
    actor Usuario
    Usuario ->> GestorProductos: agregarProducto()
    GestorProductos ->> Producto: new Producto()
    GestorProductos ->> Stock: verificarStock()
    Stock -->> GestorProductos: estadoStock
    GestorProductos ->> Ticket: generarTicket(items)
    Ticket ->> Descuento: aplicar(precio)
    Ticket -->> GestorProductos: totalFinal
    GestorProductos -->> Usuario: mostrar ticket y precio final
