# EJERCICIO:
# ¡Deadpool y Wolverine se enfrentan en una batalla épica!
# Crea un programa que simule la pelea y determine un ganador.
# El programa simula un combate por turnos, donde cada protagonista posee unos
# puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
# de regeneración y evasión de ataques.
# Requisitos:
# 1. El usuario debe determinar la vida inicial de cada protagonista.
# 2. Cada personaje puede impartir un daño aleatorio:
#    - Deadpool: Entre 10 y 100.
#    - Wolverine: Entre 10 y 120.
# 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
# siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
# 4. Cada personaje puede evitar el ataque contrario:
#    - Deadpool: 25% de posibilidades.
#    - Wolverine: 20% de posibilidades.
# 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
# Acciones:
# 1. Simula una batalla.
# 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
# 3. Muestra qué pasa en cada turno.
# 4. Muestra la vida en cada turno.
# 5. Muestra el resultado final.
import random
import time


vida_deadpool = int(input("Ingrese la vida inicial de Deadpool(min 100): "))
vida_wolverine = int(input("Ingrese la vida inicial de Wolverine(min 100): "))

if vida_deadpool < 100:
    vida_deadpool = 100
    print("Vida de deadpool ingresada menor a ¡100!")
    print("Vida actualizada, sera igual a", vida_deadpool)

if vida_wolverine < 100:
    vida_wolverine = 100
    print("Vida de wolverine ingresada menor a ¡100!")
    print("Vida actualizada, sera igual a", vida_wolverine)

turno = 1
danno_D = True
danno_W = True

while True:
    print("###########################################")
    print(f"Turno {turno}\n")
    print(f"Vida de Deadpool: {vida_deadpool}")
    print(f"Vida de Wolverine: {vida_wolverine}\n")

    # Daño de Deadpool
    if danno_W == True:
        danno_deadpool = random.randrange(10, 100)
    else:
        danno_deadpool = 0
        print("Daño maximo recibido, deadpool se esta recuperando".upper())

    # Daño de Wolverine
    if danno_D == True:
        danno_wolverine = random.randrange(10, 120)
    else:
        danno_wolverine = 0
        print("Daño maximo recibido, wolverine se esta recuperando".upper())

    # Daño maximo deadpool
    if danno_deadpool == 100:
        danno_D = False
        print("Daño de deadpool:", danno_deadpool)
        print("Daño maximo recibido, Wolverine no puede atacar en el siguiente turno")
    else:
        danno_D = True
        print(f"Daño de deadpool: {danno_deadpool}" )
        
    # Daño maximo wolverine
    if danno_wolverine == 120:
        danno_W = False
        print("Daño de wolverine:", danno_wolverine)
        print("Daño maximo recibido, Deadpool no puede atacar en el siguiente turno\n")
    else:
        danno_W = True
        print(f"Daño de wolverine: {danno_wolverine}\n")

    # Vida despues de la batalla
    probabilidad_deadpool = random.random()
    probabilidad_wolverine = random.random()

    if probabilidad_deadpool <= 0.25:
        print("Deadpool evito el ataque de Wolverine")
    else:
        vida_deadpool -= danno_wolverine

    if probabilidad_wolverine <= 0.2:
        print("Wolverine evito el ataque de Deadpool")
    else:
        vida_wolverine -= danno_deadpool

    # Turnos
    turno = turno + 1

    # Final de la battalla
    if vida_deadpool <= 0:
        print("Wolverine ha ganado con", vida_wolverine ,"de vida")
        print("Batalla finalizada")
        break
    if vida_wolverine <= 0:
        print("Deadpool ha ganado con", vida_deadpool, "de vida")
        print("Batalla finalizada")
        break
    
    # Tiempo de espera entre turnos
    print(F"Turno {turno -1} finalizado")
    time.sleep(2)
