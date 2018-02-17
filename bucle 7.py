import sys

lim1=int(input("Escriba un numero entero: "))
lim2=int(input(f"Escriba un numero mayor que {lim1}: "))

suma=0

if (lim1>lim2):
         sys.exit()
else:     
     for n in range(lim1,lim2+1 ):
          suma=suma+n
          print(f"La suma desde {lim1} hasta {lim2} es{suma}")
          
