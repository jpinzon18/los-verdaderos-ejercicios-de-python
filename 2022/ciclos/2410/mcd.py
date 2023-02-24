
numero=int(input('ingrese un numero'))
m=int(input('ingrese segundo numero'))
while not (m == 0):
    a=numero
    b=m
    if numero <0:
        numero=-a
        m=b
    if m < 0:
        numero=a
        m=-b
    else:
        numero= b
        m= a%b
print(numero)


