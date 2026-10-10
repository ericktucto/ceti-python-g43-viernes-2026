ARCHIVO = 'tareas.txt'

def agregar_tarea(tareas, texto):
    pass

def marcar_completada(index, tareas):
    pass


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
