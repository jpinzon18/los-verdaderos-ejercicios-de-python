nota = float(input("ingrese la nota:"))


if nota >=0 and nota <=3:
    print ("RECUPERACION")
elif nota >=4 and nota <=6:
    print ("INSUFICIENTE")
elif nota >=7 and nota <=7.9:
    print ("NOTABLE")
elif nota >=8 and nota <=8.9:
    print ("BIEN")
elif nota >=9 and nota <=10:
    print ("SOBRESALIENTE")
else:
    print ("el numero no es valido")
             