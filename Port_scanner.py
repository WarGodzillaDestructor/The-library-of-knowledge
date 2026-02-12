import socket

def escanear_puerto(ip, puerto):
    s = socket.socket()
    try:
        s.connect((ip, puerto))
        s.close()  # ← Paréntesis
        return True
    except:
        s.close()  # ← Paréntesis
        return False

def escanear_rango(ip, puerto_inicio, puerto_fin):
    print(f"Escaneando {ip}...")  # ← f-string
    
    for puerto in range(puerto_inicio, puerto_fin + 1):  # ← puerto, no ip
        if escanear_puerto(ip, puerto):
            print(f"Puerto {puerto} abierto")
    
    print("\nEscaneo completo!")

# Programa principal
ip = input("IP o dominio: ")
puerto_inicio = int(input("Puerto inicial: "))
puerto_fin = int(input("Puerto final: "))

escanear_rango(ip, puerto_inicio, puerto_fin)