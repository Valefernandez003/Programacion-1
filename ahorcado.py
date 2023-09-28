import random

# Lista de palabras para adivinar
words = ["programacion", "python", "javascript", "computadora", "programador", "desarrollo"]

# Función para seleccionar una palabra al azar
def select_random_word():
    return random.choice(words)

# Función para mostrar el tablero
def display_board(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Función para jugar una partida
def play_game():
    secret_word = select_random_word()
    guessed_letters = []
    attempts = 6  # Número de intentos

    while attempts > 0:
        print("\n" + display_board(secret_word, guessed_letters))
        guess = input("Ingresa una letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Ingresa una sola letra válida.")
            continue

        if guess in guessed_letters:
            print("Ya has adivinado esa letra antes.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("¡Adivinaste una letra!")
        else:
            attempts -= 1
            print(f"Letra incorrecta. Te quedan {attempts} intentos.")

        if set(secret_word) == set(guessed_letters):
            print(f"\n¡Felicitaciones! Has adivinado la palabra: '{secret_word}'.")
            break

    if attempts == 0:
        print("\n¡Oh no! Te quedaste sin intentos. La palabra era:", secret_word)

# Función principal para el juego
def main():
    print("¡Bienvenido al juego del ahorcado!")
    play_game()
    
if __name__ == "__main__":
    main()

