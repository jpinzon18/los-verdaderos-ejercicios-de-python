import random
prom=0
sum=0
rango=random.randint(10,25)
vec=[round(random.random()*100)for i in range(rango)]
for i in range(rango):
    sum+=vec[i]
print(sum)
prom=sum//rango
print('el rango de la lista es:',rango)
print('los valores de la lista son:',vec)
print('el promedio de los valores es:',prom)

for n in vec:
    if n<prom:
        print('el numero',n,'es menor al promedio')
    elif n>prom:
        print('el numero',n,'mayor al promedio')
    elif n==prom:
        print('el numero ',n,'es igual al promedio')
                 