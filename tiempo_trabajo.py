
import time, os
tiempo = 1500
descanso = 300

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def tiempo_descansar(d):
    limpiar_pantalla()
    for i in range(d, 0, -1):
        limpiar_pantalla()
        mins, secs = divmod(i, 60)
        print(f"Tiempo restante: {mins:02d}:{secs:02d}")

        print(f"Tiempo de descanso restante: {i}")
        time.sleep(1)

    os.system('afplay /System/Library/Sounds/Glass.aiff')

def tiempo_trabajar(t):
    limpiar_pantalla()
    for i in range(t, 0, -1):
        
        mins, secs = divmod(i, 60)
        print(f"TIEMPO DE TRABAJO: {mins:02d}:{secs:02d}")
        time.sleep(1)

    os.system('afplay /System/Library/Sounds/Glass.aiff')

    usuario_input2 = input("Quieres continuar o no? si para continuar, no para descansar").lower()
    if usuario_input2 == "si":
            return tiempo_trabajar(tiempo)
    elif usuario_input2 == "no":
            tiempo_descansar(descanso)
    else:
            print("Error decision no admitida")


usuario_input = input("Quieres iniciar?, SI para iniciar el programa de tiempo de trabajo, NO para salirte").lower()
if usuario_input == "si":
    tiempo_trabajar(tiempo)
elif usuario_input == "no":
    print("saliendo...")
    exit()


            