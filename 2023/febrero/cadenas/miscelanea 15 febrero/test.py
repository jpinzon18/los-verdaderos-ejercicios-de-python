def mayus():
    cadena1=(input("ingrese los elementos de la cadena : "))
    thecadena_upper=cadena1.upper()
    print(thecadena_upper)

def minus():
    cadena2=(input("ingrese los elementos de la cadena: "))
    cadena2_lower=cadena2.lower()
    print(cadena2_lower)

def firstmayus():
    cadena3=(input("ingrese los elementos de la cadena: "))
    cadena3_capitalize=cadena3.capitalize()
    print(cadena3_capitalize)
    

menu1=print("presione 1 para pasar la cadena de minuscula a mayuscula")
menu2=print("presione 2 para pasar la cadena de mayuscula a minuscula")
menu3=print("presione 3 para que solo el primer elemento de la cadena pase a mayuscula")

number=(input("presione el numero correspondiente a la opcion que desea usar: "))

match number:
 case 1:
    if number==1:
       mayus()
 case 2:
    if number ==2:
     minus()
 case 3:
    if number==3:
      firstmayus()


vocales=["a","e","i","o","u"]
 consonantes=["p","q", "b", "t", "d", "c", "ch", "j", "k", "g", "f", "y", "s", "z", "m", "n", "ñ", "l", "x", "r", "w", "y"]
 vocales_con_tilde=["á","é","í","ó","ú"]
 
 cadena=input("ingrese la cadena:")
 cadena2=input("ingrese la cadena:")
 cadena3=input("ingrese la cadena:")
 cadena4=input("ingrese la cadena:")
 cadena5=input("ingrese la cadena:")
 cadena6=input("ingrese la cadena:")
 cadena7=input("ingrese la cadena:")
 cadena8=input("ingrese la cadena:")
 cadena9=input("ingrese la cadena:")
 cadena10=input("ingrese la cadena:")
 cad=[]
 cad.append(cadena)
 cad.append(cadena2)
 cad.append(cadena3)
 cad.append(cadena4)
 cad.append(cadena5)
 cad.append(cadena6)
 cad.append(cadena7)
 cad.append(cadena8)
 cad.append(cadena9)
 cad.append(cadena10)  