class Descuento :
    def __init__(self,tipo, porcentaje):
        self.tipo=tipo
        self.porcentaje=porcentaje

    def aplicar(self,precio):
        if self.tipo.lower()=="efectivo":
            return precio-(precio*10/100)
        elif self.tipo.lower()=="credito":
            return precio+(precio*15/100)
        return precio