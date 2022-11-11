import random

vector=[]
suma=0
promedio=0
cont=0
rango=random.randint(10,25)
for i in range(rango):
    vector.append(round(random.random()*100))
    suma+=vector[i]
    promedio=suma//rango
print('el rango de la lista es: ', rango)
print('los valores de la lista son:' ,vector)
print('el promedio de los valores es: ',promedio)

for n in vector:
    if n<promedio:
        print('el numero',n,'es menor al promedio')
    elif n>promedio:
        print('el nuemro',n,'es mayor al promedio')
    elif n==promedio:
        print('el numero',n,'es igual al promedio')
                 