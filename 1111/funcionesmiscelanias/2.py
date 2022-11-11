

def cifras(numero):
    if numero >=0 and numero <=0:
        return "el numero tiene 1 cifra"
    elif numero <=0 and numero <=99:
        return  "el numero tiene 2 cifras"
    elif numero >=100 and numero <=999:
        return  "el numero tiene 3 cifras"
    elif numero >=1000 and numero <=9999:
        return  "el numero tiene 4 cifras"
    else:
        return  "el numero no es valido"

print (cifras(567))
