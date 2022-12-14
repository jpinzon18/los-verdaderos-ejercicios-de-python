import random

vector=[]
aux=True
A=0
B=0
C=0
while aux:
    rango=int(input('elija la cantidad de elementos a ejecutar de la serie de fibonaccci: '))
    if rango>=5 and rango<=20:
        aux=False
    else:
        print('deben de ser minimo 5 elementos y maximo 20')

for i in range(rango):
    C=A+B
    A=B
    B=C
    vector.append(C)
print('lalista con los valores de fibonacci hasta la posicion insertada es:',vector)
    