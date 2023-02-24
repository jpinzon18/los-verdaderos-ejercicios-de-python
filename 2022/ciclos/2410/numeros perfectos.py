for numero in range(1,1000):
    i=1
    contador=0
    while(numero > i):
      if numero%i ==0:
        contador+=1
      i+=1
      if numero == contador:
        print("el numero ", numero, "es perfecto")
