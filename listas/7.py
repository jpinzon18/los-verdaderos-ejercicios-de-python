import random

vector=[]
suma=0
promedio=0
rango=random.randint(10,25)
for i in range(rango):
    vector.append(round(random.random()*100))
    suma+=vector[i]
    promedio=suma//rango
print('el rango de la lista es:',rango)
print('los elementos de la lista son:',vector)
print('la suma de los elemento de la lista es:',suma)
print('el promedio de los elementos de la lista es:',promedio)
    