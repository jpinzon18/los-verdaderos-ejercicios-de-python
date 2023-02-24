<<<<<<< HEAD
menu1=print("presione 1 para pasar la cadena de minuscula a mayuscula")
menu2=print("presione 2 para pasar la cadena de mayuscula a minuscula")
menu3=print("presione 3 para que solo el primer elemento de la cadena pase a mayuscula")
try:
 number=(int(input("presione el numero correspondiente a la opcion que desea usar: ")))
except ValueError:
    print("el dato ingresado no esta soportado reinicie el programa")
    
def mayus():
    cadena1=(input("ingrese los elementos de la cadena : "))
    thecadena_upper=cadena1.upper()
    print("la palabra pasada a mayusculas es:",thecadena_upper)

def minus():
    cadena2=(input("ingrese los elementos de la cadena: "))
    cadena2_lower=cadena2.lower()
    print("La palabra pasada a minusculas es:",cadena2_lower)

def firstmayus():
    cadena3=(input("ingrese los elementos de la cadena: "))
    cadena3_capitalize=cadena3.capitalize()
    print("la primera letra de la cadena pasada a mayusculas es:",cadena3_capitalize)

try:
 if number==1:
     mayus()
 elif number==2:
     minus()
 if number==3:
     firstmayus()
except NameError:
    print("")    
=======
def mayo():
    cadena1=(input("ingrese los elementos de la cadena : "))
    thecadena_upper=cadena1.upper()
    print(thecadena_upper)


mayo()
>>>>>>> fca79ac4c5c9cbb26d14dad51e2d3152691adb12
