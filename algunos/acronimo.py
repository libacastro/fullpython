
from typing import final


frase = input("ingresa tu frase y te haremos un acronimo\n: ")
fraseList = frase.split()

i = 0
cont = len(fraseList)
last = ""

while (i < cont):

    palabra = list(fraseList[i])
    last = last + palabra[0]
    i = i+1

last = last.upper()
print(f'tu acronimo es "{last}"')



