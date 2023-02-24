def agregate():
 try:
     pal=int(input("ingrese los numeros que quiera agregar a una lista: "))
     lista=[]
     lista.append(pal)
     print(f"la lsita con los elementos agregados es: ",lista)
     agregate()
 except ValueError:
     print("no ingresaste un numero o un dato valido vuelve a ejecutar el programa")

agregate()