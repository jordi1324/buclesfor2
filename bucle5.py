import sys

cont=int(input("Cuantos valores va a introducir:  "))
num=0
n=0
co=0
c=cont
while (cont>0):
     for n in range(0,cont):
          n=n+1
          num=int(input(f"Escriba el numero {n}: "))
          if (num>0):
               co=co+1
          if (c==n):
               co=co-1
               print(f"Has escrito {co} numeros negativos")
               sys.exit()
     
          
