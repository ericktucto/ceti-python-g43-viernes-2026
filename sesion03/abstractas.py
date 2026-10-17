from abc import ABC
from abc import abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando con tarjeta... S/ {monto}")

# mp = MetodoPago() # Tira error por que es una clase abstracta
mp = PagoTarjeta()

mp.pagar(12)
