class Stock:
    def __init__(self,cantidadDisponible:int,alerta:bool):
        self.cantidadDisponible=cantidadDisponible
        self.alerta=alerta

    def verifica(self) -> bool:
        self.alerta = self.cantidadDisponible <= 10
        return self.alerta
