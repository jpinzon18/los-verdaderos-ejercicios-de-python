<<<<<<< HEAD
print("creo que si sirve")

print(__name__)


def pitagoras(cateto1,cateto2):
    re1=cateto1**2
    re2=cateto2**2
    h=(re1+re2)**0.5
    return h


def parimpar(num):
    if num%2==0:
        print('par')
    else:
        print('impar')


def divisores(numero):
    suma=0
    for i in range(1,numero):
       if numero%i==0:
          suma+=i
    return suma


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


def suma():
    num1=int(input('ingrese el primer numero: '))
    num2=int(input('ingrse  el segundo numero: '))
    print(num1+num2)
    
    

     
                       
                   
  



=======
print("creo que si sirve")

print(__name__)


def pitagoras(cateto1,cateto2):
    re1=cateto1**2
    re2=cateto2**2
    h=(re1+re2)**0.5
    return h


def parimpar(num):
    if num%2==0:
        print('par')
    else:
        print('impar')


def divisores(numero):
    suma=0
    for i in range(1,numero):
       if numero%i==0:
          suma+=i
    return suma


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


def suma():
    num1=int(input('ingrese el primer numero: '))
    num2=int(input('ingrse  el segundo numero: '))
    print(num1+num2)
    
    

     
                       
                   
  



>>>>>>> fca79ac4c5c9cbb26d14dad51e2d3152691adb12
