valor = 0
for numero in range (100, 1000):
    valor = numero
    u=numero%10
    numero=numero//10
    d=numero%10
    numero=numero//10
    c=numero%10
    u**=3
    d**=3
    c**=3
    suma = u+d+c
    if suma == valor:
        print (valor)
        

