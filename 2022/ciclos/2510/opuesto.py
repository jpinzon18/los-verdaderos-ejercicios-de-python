numero = 1
cont=0
while True:
    numero= int(input('ingrese un  numero: '))
    contra=numero*-1
    if numero==0:
        print('la cantidad de numero puests fue: ',cont)
        break
    elif numero>0:
         print ('el numero es ',numero,'y su contrario es',contra)
    else:
        print ('el numero es',numero,'y su contrario es',contra)
    cont+=1         