i=1
cont = 0
suma = 0

numero= int(input("ingrese numero"))

while(numero>i):
 if numero%1 ==0:
    cont=i  
 i+=1

for i in range(cont+1):
 suma+=i

 if numero == suma:
    print("el numero", numero, "es perfecto")
 else:
    print("el numero", numero, "no es perfecto")   