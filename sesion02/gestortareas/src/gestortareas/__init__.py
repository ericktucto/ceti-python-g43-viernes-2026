from gestortareas.tareas import cargar_tareas
from gestortareas.tareas import guardar_tareas
lista_tareas = []

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar como completada")
    print("4. Salir (guardando)")

AGREGAR_TAREA = 1
LISTAR_TAREAS = 2

def main() -> None:
    lista_tareas = cargar_tareas()
    print(lista_tareas)
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("La opcion no es valida")
            continue
        
        if opcion == AGREGAR_TAREA:
            continue
        elif opcion == LISTAR_TAREAS:
            continue
        elif opcion == 3:
            continue
        elif opcion == 4:
            guardar_tareas(lista_tareas)
            break
        else:
            print("La opcion no es valida")
