from imostrable import IMostrable
class Usuario(IMostrable):
    def __init__(self,nombre:str,dni:str,id:str):
        self.nombre=nombre
        self.dni=dni
        self.id=id
    def mostrar(self):
        print(f"Usuario: {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"ID: {self.id}")

    