try:
 def sumasimple():
     dig1=int(input("ingrese el primer digito: "))
     dig2=int(input("ingrese el sefungo digito: "))
     sum=(dig1+dig2)
     print ("el resultado es: ",sum)

 sumasimpl()
except NameError:
    print("No se invoco a la funcion correctamente")
else:
    print("reinicie el programa")

