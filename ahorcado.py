import random

palabras = ["naranja","jabon","lemur","tucan"]
palabra = random.choice(palabras)
palabra2 = list(palabra)
largo = len(palabra)
palabra3 = {"a","b","d","z","g"}
incognita = []
vida = 10
print(f" ".join(palabra2))
print(type(palabra3))

for x in palabra:
    incognita.append("_ ")

print(f"tu palabra tiene {largo} letras")
contador = palabra.count("a")
"""
while vida > 0 and palabra != incognita:
    print(incognita)
    letra = input("introduce una letra: ")
    if letra in palabra:
        for i in palabra:
            if i == letra:
                pos = palabra.index(i)
                incognita[pos] = i
    else:
        print("intenta de nuevo")

print("Adios!")
 
"""




