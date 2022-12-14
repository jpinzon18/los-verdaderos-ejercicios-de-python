def mate():
 try:
    b = int(input('ingrese la variable b: '))
    print("el resultado es :" ,(b**2-4)/2)
 except ValueError:
    print('no ingresaste un numero corre el programa de nuevo ')    

    
mate()    
