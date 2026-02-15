import subprocess
import qrcode
import os

#hacer que el codigo qr vaya a mi cuenta de github
CARPETA = os.path.expanduser("~/Qr_folder")
def codigo_qrSimple():
    #crear carpeta
    
    os.makedirs(CARPETA, exist_ok=True)


    img = qrcode.make("https://github.com/WarGodzillaDestructor")
    
    nombre_img = "mi_github.png"
    ruta_final = os.path.join(CARPETA, "mi_github.png")
    img.save(ruta_final)
    print(f"QR guardado en {ruta_final} ✅")

def red_existe(nombre_red):
    try:
        comando = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"]
        resultado = subprocess.check_output(comando).decode()

        return nombre_red in resultado

    except Exception as e:
        print(f"Error al buscar redes: {e}")
        return False
    
def conectar_wifi(nombre_red, contrasena):
    if not nombre_red.strip():
        print("❌ El nombre de la red no puede estar vacío.")
        return

    if len(contrasena) < 8:
        print("❌ La contraseña debe tener al menos 8 caracteres (WPA).")
        return

    if not red_existe(nombre_red):
        print("❌ No se encontró esa red WiFi disponible.")
        return
    datos_wifi = f"WIFI:S:{nombre_red};T:WPA;P:{contrasena};;"
    os.makedirs(CARPETA, exist_ok=True)
    img2 = qrcode.make(datos_wifi)
    ruta_archivo_wifi = os.path.join(CARPETA, "wifi_qr.png")
    try:
        img2.save(ruta_archivo_wifi)
        print(f"QR WiFi generado en: {ruta_archivo_wifi} 📶")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")


def generar_vcard_qr(nombre, celular, email):
    os.makedirs(CARPETA, exist_ok=True)
    
    # Formato estándar de una vCard (Versión 3.0)
    # Es muy sensible a los saltos de línea (\n)
    datos_vcard = (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"FN:{nombre}\n"          # Nombre completo
        f"TEL;TYPE=CELL:{celular}\n" # Teléfono
        f"EMAIL:{email}\n"        # Correo
        "END:VCARD"
    )

    img3 = qrcode.make(datos_vcard)
    ruta_Vcard =  os.path.join(CARPETA, "mi_contacto.png")
    img3.save(ruta_Vcard)
    print(f"QR de Contacto (vCard) guardado en: {ruta_Vcard} 📇")

def texto_simple():
    os.makedirs(CARPETA, exist_ok=True)
    img4 = qrcode.make("Hola")
    ruta_Texto_simple = os.path.join(CARPETA, "Texto_simple.png")
    img4.save(ruta_Texto_simple)
    print(f"QR de texto guardado en: {ruta_Texto_simple}")
def main():
    while True:
        opcion = input("Elige hacer codigo qr de que \n opcion 1: codigo qr simple que te redirije a mi github \n opcion 2: codigo qr que te conecta a red wifi \n opcion 3: codigo qr que te dirije a un contacto \n opcion 4: codigo qr que te redirije a un texto simple \n O pon salir para salir").lower()
        if opcion == "1":
            codigo_qrSimple()
        elif opcion == "2":
            nombre_red = input("Nombre de la red")
            contrasena = input("contrasena de la red")
            conectar_wifi(nombre_red, contrasena) #pon el nombre de tu red y wifi si no lo haces no funcionara(hice esto para evitar que mi red wifi se compartiera y se usara para mal uso)  
        elif opcion == "3":
            nombre = input("Nombre del contacto")
            celular = input("numero de telefono del contacto")
            email = input("email del contato")
            generar_vcard_qr(nombre, celular, email) #pon el nombre del contacto el numero de telefono y gmail (No me hago culpable de como uses este, es tu responsabilidad y debes usarlo de forma etica)
        elif opcion == "4":
            texto_simple() #Escribe el texto
        elif opcion == "salir":
            break

if __name__ == "__main__":
    main()