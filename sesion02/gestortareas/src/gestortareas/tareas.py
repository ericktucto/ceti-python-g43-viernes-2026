ARCHIVO = 'tareas.txt'

def agregar_tarea(tareas, texto):
    tareas.append({
        "texto": texto,
        "hecha": False
    })

def listar_tareas(tareas):
    """
        1 [ ] <texto>
        2 [x] <texto>
    """
    contador = 1
    print("-" * 25)
    for tarea in tareas:
        brackets = "[x]" if tarea["hecha"] else "[ ]"
        print(f"{contador}) {brackets} {tarea['texto']}")
        contador += 1
    print("-" * 25)

def marcar_completada(opcion, tareas):
    tareas[opcion - 1]["hecha"] = True
    texto = tareas[opcion - 1]["texto"]
    print(f"Tu tarea '{texto}' fue marcada como completada")


def cargar_tareas():
    tareas = []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            hecha, texto = linea.split("|")
            tareas.append({
                "texto": texto,
                "hecha": True if hecha == "1" else False
            })
    return tareas

def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            hecha = "1" if tarea["hecha"] else "0"
            archivo.write(f"{hecha}|{tarea['texto']}\n")
