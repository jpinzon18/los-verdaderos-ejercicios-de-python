import random

vec=[]
veccant=[]
rango=random.randint(10,25)

for i in range(rango):
    vec.append(round(random.random()*100))
print(vec)
cont=0
for i in range (len(vec)):
    cont=0
    for j in vec:
        if vec[i] == j:
            cont+=1
    if cont!=0:
        veccant.append(cont)
    else:
        veccant.append(0)
print(vec)
print(veccant)
mayor=0
pos=0
for i in range(len(vec)):
    if mayor<veccant[i]:
       mayor=veccant[i]
print('el mayor es ',mayor)
for j in range (len(veccant)):
    if mayor==veccant[j]:
        print('la moda es ',vec[j])
                                  
