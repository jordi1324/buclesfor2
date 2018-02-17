import sys
cont=int(input("Cuantos valores va a introducir:  "))
num=0

while (cont>0 and cont>num):
     if (cont<0):
          print("Impossible")
          break
     for n in range(0,cont):
          num=int(input("Escriba un numero  mas grande que el primero que ha introducido:  "))
          if (cont>num):
               print("El numero que ha introducido era mas pequeno")
               print("Gracias por su colaboracion")
               sys.exit()
