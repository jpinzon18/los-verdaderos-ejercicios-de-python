i=1
suma=0
print("intriduce una serie de numeros.\ si es 0 se terminara la lista",end="\n" )

print ("numero",i,":",end="")
numero=eval(input())
print(numero)
suma=suma+numero

while numero !=0:
    i=i+1
    print("numero",i,":",end="")
    numero=eval(input())
    print(numero)
    suma=suma+numero
    
print("la suma de los numeros es: ",suma)
    