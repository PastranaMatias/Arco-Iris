class Stock:
    def __init__(self,cantidadDisponible:int):
        self.cantidadDisponible=cantidadDisponible
        self.alerta=True    #modifique la variable para que inicie
                            #como verdadero

    def verifica(self) -> bool:

        if self.cantidadDisponible <= 0:
            self.alerta = False
            print("No hay Stock= 0")
        
        return self.alerta
