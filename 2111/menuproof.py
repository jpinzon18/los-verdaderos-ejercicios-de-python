ctrl=(input('presione el numero con la funcion que quiera usar '))

match ctrl:
 case 1:
      cap=(input('ingrese 1 para ver la lista de canciones '))
      if cap == 1:
        print (spotify)  
 case 2 :
     cap2=(input('ingrese 2 para ver las lista de favoritos '))
     if cap2 == 2:
         listafav()
 case 3:
     cap3=(input('ingrese 3 para dar ppt finalizado el programa '))
     if cap3 == 3:
         print('aqui acaba el programa')
         
         