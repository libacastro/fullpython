#inicio

from doctest import ELLIPSIS_MARKER


def main():
    palabra = input("Escribe una palabra: ")
    palabra = palabra.replace(" ","")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Tu palabra es un palindromo")
    else:
        print("Tu palabra no es un palindromo")


def palindromo(word):
    reversa = word[::-1]
    if reversa == word:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
