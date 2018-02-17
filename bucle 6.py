from turtle import *
import sys

setup(640,480,0,0)
title("bucle 6")

cont=int(input("Cuantos valores va a introducir:  "))
num=0
n=0
co=0
c=cont
pos=0
imp=0

while (cont>0):
     for n in range(0,cont):
          n=n+1
          num=int(input(f"Escriba el numero {n}: "))
          if( num%2):
               pos=pos+1
          else:
               imp=imp+1
          if (c==n):
               print(f"Has escrito {imp} numeros pares y {pos} impares")
               sys.exit()
     
