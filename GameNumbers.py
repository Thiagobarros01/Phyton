#from asyncore import read
from random import Random, randint, random
#import this 
#from tkinter.tix import INTEGER
#mini game, ache o número

x = randint(0,50)
n = -1
cont = 0

while n != x:
   cont = cont+1
   n = int(input("digite um numero: ")) 
   if n > x:
    print("Você digitou um número maior")
   elif n < x:
    print("Você digitou um númeo menor")
   elif n == x:
        print("Parabéns, você achou!")    
        print(f"Você usou {cont} tentativas ")
        
#tabuada 1 a 10