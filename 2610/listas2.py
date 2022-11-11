import random
cont1=0
cont2=0
totalpar=0
totalimpar=0
prompar=0
promimpar=0
tam=int(input('Cuantos numeros'))
vector=[]
for i in range (tam):
    vector.append(round(random.random()*100))
print(vector)

for i in range (tam):
    #print('posicion ' ,i, 'elemento ' ,vector[i])
    if vector [i]%2==0:
       print(vector[i],'es par')
       cont1+=1
       totalpar+=vector[i]
       prompar=totalpar//cont1
    else:
        print(vector[i],'es impar')
        cont2+=1
        totalimpar+=vector[i]
        promimpar=totalimpar//cont2
        
print('la cantidad total de pares fueron:',cont1,'y la cantidad de impares totales fueron: ',cont2)
print('la suma de los pares es:',totalpar,'y la suma de los impares es:',totalimpar)
print('el promedio de los pares es',prompar,'el promedio de los impares:',promimpar)
       
           