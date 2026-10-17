class Client:
    def __init__(self, saldo, nombre):
        self._saldo = saldo
        self.__nombre = nombre

    # getter
    def getSaldo(self):
        return self._saldo

    def getNombre(self):
        return self.__nombre

    # setter
    def setSaldo(self, nuevo_saldo):
        self._saldo = nuevo_saldo if nuevo_saldo >= 0 else 0

    def setNombre(self, nombre: str):
        if nombre.strip() == "":
            raise ValueError("No puede estar vacio el nombre")
        self.__nombre = nombre

    

cliente1 = Client(3000, "Ana")

print("Tu saldo es:", cliente1.getSaldo())

nuevo_saldo = -100

cliente1.setSaldo(nuevo_saldo)
#cliente1.setNombre("")

print("Tu saldo cambio:", cliente1.getSaldo())

cliente1.__nombre = "Jorge"
cliente1.edad = 18

print("Tu nombre:", cliente1.__nombre)
print("Tu nombre:", cliente1.getNombre())
print(cliente1.edad)


class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre

    # getter
    @property
    def nombre(self):
        return self.__nombre

    # setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("No puede estar vacio el nombre")
        self.__nombre = nuevo_nombre



usuario1 = Usuario("John")

print("Nombre del usuario:", usuario1.nombre)

usuario1.nombre = "Pedro"

print("Tu nuevo nombre es:", usuario1.nombre)