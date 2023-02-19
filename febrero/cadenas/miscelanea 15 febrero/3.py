def repeticion():
    cadena1=(input("ingrese el primer elemento de la cadena: "))
    cadena2=(input("ingrese el segundo elemento de la cadena: "))
    lst=[]
    lst.append(cadena1)
    lst.append(cadena2)

    letra=(input("ingrese la letra de la cual desea saber la repeticion:"))
    
    for letra in lst:
     print(lst.count(letra))

    if letra not in lst:
        print("la letra ingresada no esta en la cadena")
    elif letra in lst:
        print("la letra ingresada esta en la cadena")  

repeticion()