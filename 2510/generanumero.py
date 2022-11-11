import random

r=(round(random.random()*100))
cont=0
while True:
    n = int(input('ingrese un numero: '))
    cont+=1
    if n>r:
        print('el numero es menor, intentelo de nuevo')
    elif  n<r:
        print('el numero es mayor, intentelo de nuevo')
    else:
        print('felicidades,encontro el numero, las veces que lo ha intentado fueron:',cont)
        break
