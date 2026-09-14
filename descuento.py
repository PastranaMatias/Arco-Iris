class Descuento :
    def __init__(self,tipo, porcentaje):
        self.tipo=tipo.lower()
        self.porcentaje=porcentaje

    def aplicar(self,precio):
        if self.tipo=="efectivo":
            return precio-(precio*self.porcentaje/100)
        elif self.tipo=="credito":
            return precio+(precio*self.porcentaje/100)
        return precio