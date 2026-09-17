from datetime import date

class Ticket:    
    def __init__(self):
        self.items=[]  #(id produ y cantidad)

    def agregarP(self,pro,can):
        print("agregando:",pro.nombre,can)
        self.items.append((pro,can))  #agrego el producto y la canti

    def calTotal(self):
        total=0
        for produc, cant in self.items:
            total+=produc.precio*cant    #(mult por la cantidad)
        return total

    def impriTiket(self):
        print("== Tiket ==")
        for li,ca in self.items:
            print(f"{li.nombre} x{ca} ${li.precio*ca}")
