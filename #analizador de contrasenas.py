# Analizador de contraseñas
def analizar_password(password):
    score = 0
    problemas = []
    
    # LONGITUD (if independientes, no elif)
    if len(password) < 8:
        problemas.append("Muy corta (mínimo 8)")
    
    if len(password) >= 8:
        score += 2
    if len(password) >= 12:
        score += 2
    if len(password) >= 16:
        score += 1
    
    # MAYÚSCULAS
    tiene_mayuscula = any(c.isupper() for c in password)
    if tiene_mayuscula:
        score += 1
    else:
        problemas.append("Sin mayúsculas")
    
    # MINÚSCULAS
    tiene_minuscula = any(c.islower() for c in password)
    if tiene_minuscula:
        score += 1
    else:
        problemas.append("Sin minúsculas")
    
    # NÚMEROS
    tiene_numero = any(c.isdigit() for c in password)
    if tiene_numero:
        score += 1
    else:
        problemas.append("Sin números")
    
    # SÍMBOLOS
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    tiene_simbolo = any(c in simbolos for c in password)
    if tiene_simbolo:
        score += 2
    else:
        problemas.append("Sin símbolos")
    
    # CLASIFICAR
    if score <= 3:
        nivel = "MUY DÉBIL ❌"
    elif score <= 5:
        nivel = "DÉBIL ⚠️"
    elif score <= 7:
        nivel = "MEDIO 🟡"
    else:
        nivel = "FUERTE ✅"
    
    return nivel, score, problemas

# Programa principal
password = input("Password a analizar: ")
nivel, score, problemas = analizar_password(password)

print(f"\n{nivel}")
print(f"Score: {score}/10")

if problemas:
    print("\nProblemas:")
    for problema in problemas:
        print(f"  - {problema}")