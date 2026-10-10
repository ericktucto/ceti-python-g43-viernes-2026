class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def presentarse(self, saludo = "Hola"):
        return f"{saludo}, soy {self.nombre}"


class Pagable():
    def pagar(self):
        raise Exception("No implementastes el metodo pagar")


class PagarTarjeta(Pagable):
    def pagar(self):
        return "Estoy pagango con una tarjeta de credito"


class PagarYape(Pagable):
    def pagar(self):
        return "Estoy pagango con yape"



def checkout(pagable: Pagable):
    print(pagable.pagar())



usuario1 = Usuario("Ana", "ana@testing.com")
tarjeta = PagarTarjeta()

checkout(usuario1)

