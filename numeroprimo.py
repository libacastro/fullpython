
def es_primo(numero):
    contador = 0

    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1

    if contador == 0 and numero != 1:
        return True
    else:
        return False


def main():
    num = int(input('ingrese un número: '))
    if es_primo(num):
        print('Es un número primo')
    else:
        print('No es un número primo')



if __name__ == '__main__':
    main()