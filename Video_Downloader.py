import yt_dlp

opciones = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s', # Nombre del archivo
}

print("pon la url del video de youtube que quieres descargar")
url = input()
def descargar_videos(url):
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])
descargar_videos(url)