def determinar_ganador(eleccion_ines, eleccion_juan):
    """
    Determina el ganador del juego basado en las elecciones de Inés y Juan.
    """
    resultados = {
        ("piedra", "tijera"): "Inés gana.",
        ("tijera", "piedra"): "Juan gana.",
        ("tijera", "papel"): "Inés gana.",
        ("papel", "tijera"): "Juan gana.",
        ("papel", "piedra"): "Inés gana.",
        ("piedra", "papel"): "Juan gana.",
    }
    
    if eleccion_ines == eleccion_juan:
        return "Nadie, es un empate."

    return resultados.get((eleccion_ines, eleccion_juan), "Elección inválida.")

def main():
    print("¡Bienvenidos al juego de Piedra, Papel o Tijera!")

    # Obtener la elección de Inés
    eleccion_ines = input("Inés, elige Piedra, Papel o Tijera: ").strip().lower()
    if eleccion_ines not in ["piedra", "papel", "tijera"]:
        print("Elección inválida. Fin del juego.")
        return
    
    # Obtener la elección de Juan
    eleccion_juan = input("Juan, elige Piedra, Papel o Tijera: ").strip().lower()
    if eleccion_juan not in ["piedra", "papel", "tijera"]:
        print("Elección inválida. Fin del juego.")
        return

    # Determinar el ganador
    resultado = determinar_ganador(eleccion_ines, eleccion_juan)
    print(f"Inés eligió: {eleccion_ines.capitalize()}")
    print(f"Juan eligió: {eleccion_juan.capitalize()}")
    print(resultado)

if __name__ == "__main__":
    main()
