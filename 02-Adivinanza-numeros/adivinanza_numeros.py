import random

def juego():
    print("\n#################################")
    print("Bienvenido al juego de adivinanza")
    print("#################################")
    random_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("\nAdivina el número entre 1 y 100: "))
            attempts += 1
            if guess < random_number:
                print("Demasiado BAJO")
            elif guess > random_number:
                print("Demasiado ALTO")
            else:
                print(f"¡Lo lograste! El número era {random_number}.")
                print(f"Intentos: {attempts}")
                break
        except ValueError:
            print("Debes ingresar un número entero")

def main():
    while True:
        juego()
        again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if again != "s":
            break


main()