from asyncore import read
from random import Random, randint, random 
from tkinter.tix import INTEGER

print("Vamos praticar a tabuada!")
condicao = True
cont = 0
while condicao == True:
   tabuada = randint(1,10)
   numeros = randint(1,10)
   y = tabuada * numeros
   valor = int(input(f"{tabuada}x{numeros}= "))
   if valor != y:
     condicao = False
     print("infelizmente você errou!")
   else:
      cont +=1  
print(f"Você acertou {cont} vezes")