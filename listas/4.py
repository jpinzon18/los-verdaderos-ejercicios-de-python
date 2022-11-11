import random

vector=[]
rango=random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
print('la lista sin ordenar es:',vector)
intercambio=True
while intercambio:
    intercambio=False
    for i in range(len(vector)-1):
        if vector[i]>vector[i+1]:
            vector[i],vector[i+1],vector[i]
            intercambio=True

print('la lista ordenada es:',vector)

