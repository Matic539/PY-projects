import json
import os

# Menu
def menu():
    print("\n##############################")
    print(" Sistema de Gestión de Tareas")
    print("##############################\n")
    print("1. Agregar una tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir\n")

# Crear tareas
def crear_tarea(tareas):
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    while True:
        prioridad = input("Prioridad (Alta(1), Media(2), Baja(3)): ")
        if prioridad in ["1", "2", "3"]:
            if prioridad == "1":
                prioridad = "Alta(1)"
            elif prioridad == "2":
                prioridad = "Media(2)"
            elif prioridad == "3":
                prioridad = "Baja(3)"
            break
        else:
            print("Opción no valida, ingrese un numero valido")
    
    tarea = {
        "nombre": nombre,
        "descripcion": descripcion,
        "prioridad": prioridad
        }
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

# Listar tareas
def listar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"Tarea {i}:")
            print(f"Nombre: {tarea['nombre']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Prioridad: {tarea['prioridad']}")
            print("\n-------------------------------------------------\n")

# Eliminar tarea
def eliminar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas")
    else:
        listar_tareas(tareas)
        while True:
            try:
                num_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
                if 1 <= num_tarea <= len(tareas):
                    tareas.pop(num_tarea - 1)
                    print(f"Tarea {num_tarea} eliminada con éxito.")
                    break
                else:
                    print("Número de tarea no válido")
            except ValueError:
                print("Por favor, ingrese un número válido.")

def main():
    tareas = []
    while True:
        menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            os.system('cls')
            crear_tarea(tareas)
        elif opcion == "2":
            os.system('cls')
            listar_tareas(tareas)
        elif opcion == "3":
            os.system('cls')
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("Adiós...")
            break
        else:
            os.system('cls')
            print("Opción no válida. Por favor, intente de nuevo.")


main()