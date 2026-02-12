import json

def cargar_tareas():
    try:
        with open('tareas.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def mostrar_tareas(tareas):
    print("\n=== TUS TAREAS ===")
    if not tareas:
        print("No hay tareas")
        return
    for tarea, completada in tareas.items():
        if completada:
            print(f"✅ {tarea}")
        else:
            print(f"❌ {tarea}")

def agregar_tarea(tareas):
    nueva = input("Nueva tarea: ")
    tareas[nueva] = False
    print("✅ Tarea agregada!")

def completar_tarea(tareas):
    # Mostrar primero
    for tarea, completada in tareas.items():
        if completada:
            print(f"✅ {tarea}")
        else:
            print(f"❌ {tarea}")
    
    # Preguntar cuál
    cual = input("\n¿Cuál completaste?: ")
    
    # Completar
    if cual in tareas:
        tareas[cual] = True
        print(f"✅ '{cual}' completada!")
    else:
        print("❌ Esa tarea no existe")

def guardar_tareas(tareas):
    with open('tareas.json', 'w') as f:
        json.dump(tareas, f)

def todo():
    tareas = cargar_tareas()
    corriendo = True
    
    while corriendo:
        print("\n=== MENÚ ===")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Salir")
        
        user_input = input("\nElige opción: ")
        
        if user_input == "1":
            mostrar_tareas(tareas)
        elif user_input == "2":
            agregar_tarea(tareas)
            guardar_tareas(tareas)
        elif user_input == "3":
            completar_tarea(tareas)
            guardar_tareas(tareas)
        elif user_input == "4":
            guardar_tareas(tareas)
            print("👋 Adiós!")
            corriendo = False
        else:
            print("❌ Opción inválida")

todo()