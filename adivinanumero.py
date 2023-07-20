
import random

menu = "BIENVENIDO A ADIVINA EL NÚMERO"



def main():
    print(menu)
    rango = range(1,101)
    numero_azar = random.choice(rango)
    numero = int(input('Adivina el número entre el 1 y el 100: '))
    contador = 0
    
    while numero_azar != numero:
        if numero < numero_azar:
            print('El número es mayor')
            numero = int(input('Adivina el número entre el 1 y el 100: '))
            contador += 1
        elif numero > numero_azar:
            print('El número es menor')
            numero = int(input('Adivina el número entre el 1 y el 100: '))
            contador +=1
    
    contador +=1
    print(f'Ganaste!, el numero de intentos fue {contador}')
            



if __name__ == '__main__':
    main()