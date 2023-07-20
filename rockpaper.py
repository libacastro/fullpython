import random

selector = ["rock", "paper", "tijeras"]
jugar = 1
def seleccionrandom():
    return random.choice(selector)

while jugar == 1:
    usuario = input("escoge una opcion : 1)rock 2)paper 3) tijera ---> ")


    choise = seleccionrandom()
    comp = None
    if (usuario == "1"):
        comp = "rock"
    if (usuario == "2"):
        comp = "paper"
    if (usuario == "3"):
        comp = "tijeras"

    print(f"Pc escogio {choise}\ntu eleccion fue {comp}")


    if choise == comp:
        print("Empate")
    if choise == "rock" and comp == "paper":
        print("GANASTE!")
    if choise == "rock" and comp == "tijeras":
        print("PERDISTE!")

    if choise == "paper" and comp == "rock":
        print("PERDISTE!")
    if choise == "paper" and comp == "tijeras":
        print("GANASTE!")

    if choise == "tijeras" and comp == "rock":
        print("GANASTE!")
    if choise == "tijeras" and comp == "paper":
        print("PERDISTE!")
    
    jugar = int(input("quieres volver a jugar? 1)Si 2) No : "))

if jugar == 2:
    print("Adios!")

