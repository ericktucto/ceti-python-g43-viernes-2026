class BaseDeDatos:
    def desconectar(self):
        pass
try:
    cargando = True
    conexion = BaseDeDatos()
    n = int(input("Número: "))
    resultado = 10 / n
except ValueError:
    print("Eso no es un número")
except ZeroDivisionError:
    print("No se divide entre cero")  
else:
    print(f"Resultado: {resultado}")
finally:
    cargando = False
    conexion.desconectar()
    print("Siempre me ejecuto")
