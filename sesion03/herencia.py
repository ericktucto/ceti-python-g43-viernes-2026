class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def presentarse(self, saludo = "Hola"):
        return f"{saludo}, soy {self.nombre}"

    def notificar(self):
        print("Notificar por whatsapp")

class Notificable():
    def notificar(self):
        print("notificar por correo")

class Cliente(Usuario, Notificable):
    def __init__(self, nombre, correo, dni):
        super().__init__(nombre, correo)
        self.dni = dni

    def __str__(self):
        return f"-> Client(nombre={self.nombre},correo={self.correo},dni={self.dni})"


cliente1 = Cliente("Ana", "ana@testing.com", "12345647")
usuario1 = Usuario("Pedro", "pedro@testing.com")
print(cliente1.nombre)
print(cliente1.correo)
print(cliente1.dni)
cliente1.notificar()
print(Cliente.__mro__)
print("[]" + str(cliente1))
