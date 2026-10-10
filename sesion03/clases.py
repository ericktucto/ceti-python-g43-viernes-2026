class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def presentarse(self, saludo = "Hola"):
        return f"{saludo}, soy {self.nombre}"

usuario1 = Usuario("Ana", "ana@testing.com")
usuario2 = Usuario("Pedro", "pedro@testing.com")

print(usuario1.nombre)
print(usuario1.correo)
print(usuario2.presentarse("Buenos dias"))