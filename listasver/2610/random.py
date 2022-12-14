import random

vector=[]
suma=0
moda=0

rango= random.randint(10,25)
for i in range(rango):
    vector.append(round(random.random()*100))
    print(vector)
    suma+=vector[i]
    promedio=suma//rango
    
print(suma, promedio)


    