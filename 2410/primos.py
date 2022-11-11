numero=int(input("ingrese numero"))
i=1
c = 0

while(numero>i):
 if numero%1 ==0:
   c+=1
 i+=1
 if c > 2 or numero <=1:
    print("el numero No es primo")
else:
    print("el numero es primo")