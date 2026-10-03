try:
    edad = input("Dime tu edad: ")
    edad = int(edad)

    print(f"Tu edad es {edad}")
    print(f"En diez años tendras {edad + 10}")
except ValueError:
    print("La edad no es valida")
finally:
    print("Siempre me ejecuto")

