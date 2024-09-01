import random

def jugar():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    # Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    intentos = 0
    while True:
        # Obtener la entrada del usuario
        try:
            adivinanza = int(input("¿Cuál es tu adivinanza? "))
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            continue
        
        intentos += 1
        
        if adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

if __name__ == "__main__":
    jugar()
