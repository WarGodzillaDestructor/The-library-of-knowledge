# osmovercarpetas
import os 
import shutil

categorias = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "PDFs": [".pdf"],
    "Documentos": [".docx", ".txt", ".doc", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Musica": [".mp3", ".wav", ".flac"],
    "Comprimidos": [".zip", ".rar", ".7z"]
}

def obtener_categoria(extension):
    for categoria, extensiones in categorias.items():
        if extension.lower() in extensiones:
            return categoria
    return "Otros" 

def organizar_carpeta(carpeta_origen):
    archivos = os.listdir(carpeta_origen)
    
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_origen, archivo)
        
        if not os.path.isfile(ruta_completa):
            continue
        
        _, extension = os.path.splitext(archivo)
        
        categoria = obtener_categoria(extension)
        
        carpeta_destino = os.path.join(carpeta_origen, categoria)
        os.makedirs(carpeta_destino, exist_ok=True)
        
        origen = ruta_completa
        destino = os.path.join(carpeta_destino, archivo)
        shutil.move(origen, destino)
        
        print(f"✅ {archivo} → {categoria}/")

# Programa principal
carpeta = input("Carpeta a organizar: ")

if not os.path.exists(carpeta):
    print(f"❌ Carpeta no existe")
    exit()

organizar_carpeta(carpeta)
print("\n🎉 ¡Organización completa!") 