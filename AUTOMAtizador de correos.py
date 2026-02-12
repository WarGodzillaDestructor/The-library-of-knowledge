import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525
EMAIL_USER = "tu_username_mailtrap"
EMAIL_PASS = "tu_password_mailtrap"

def crear_mensaje(destinatario, contenido, asunto):
    # Crear mensaje vacío
    mensaje = MIMEMultipart()
    
    # Configurar
    mensaje['From'] = "test@example.com"
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    
    # Agregar contenido
    texto = MIMEText(contenido, 'plain')
    mensaje.attach(texto)
    
    return mensaje

def enviar_email(destinatario, asunto, contenido):
    try:
        # 1. Crear mensaje
        mensaje = crear_mensaje(destinatario, contenido, asunto)
        
        # 2. Conectar
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        # 3. Login
        server.login(EMAIL_USER, EMAIL_PASS)
        
        # 4. Enviar
        server.send_message(mensaje)
        
        # 5. Cerrar
        server.quit()
        
        print("✅ Email enviado!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# PROGRAMA PRINCIPAL
destinatario = input("Email destino: ")
asunto = input("Asunto: ")
contenido = input("Mensaje: ")

enviar_email(destinatario, asunto, contenido)
    

