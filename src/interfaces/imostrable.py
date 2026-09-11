from abc import ABC, abstractmethod

class IMostrable(ABC): 
  @abstractmethod
  def mostrar(self):
    pass