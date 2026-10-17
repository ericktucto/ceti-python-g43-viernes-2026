from gestortareas.tareas import cargar_tareas, agregar_tarea, guardar_tareas, listar_tareas, marcar_completada

lista_tareas = []

def get_opcion(mensaje):
    opcion = input(mensaje)
    try:
        return int(opcion)
    except ValueError:
        return None

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar como completada")
    print("4. Salir (guardando)")

AGREGAR_TAREA = 1
LISTAR_TAREAS = 2
MARCAR_COMPLETADA = 3
SALIR_GUARDAR = 4

def main() -> None:
    lista_tareas = cargar_tareas()
    
    while True:
        mostrar_menu()
        opcion = get_opcion("Elige una opcion: ")
        if opcion is None:
            print("La opcion no es valida")
            continue
        
        if opcion == AGREGAR_TAREA:
            texto = input("Escribi la tarea ")
            agregar_tarea(lista_tareas, texto)
            continue
        elif opcion == LISTAR_TAREAS:
            listar_tareas(lista_tareas)
            continue
        elif opcion == MARCAR_COMPLETADA:
            listar_tareas(lista_tareas)
            opcion = get_opcion("Elige una opcion: ")

            if opcion is None:
                print("La opcion no es valida")
                continue
            marcar_completada(opcion, lista_tareas)
            continue
        elif opcion == SALIR_GUARDAR:
            guardar_tareas(lista_tareas)
            break
        else:
            print("La opcion no es valida")
