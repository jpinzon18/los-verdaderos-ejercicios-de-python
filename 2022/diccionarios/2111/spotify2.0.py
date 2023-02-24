# ejercicio de spotify continuado el 21 de noviembre juan E Pinzon
spotify={
    'cancion':'cancion ingresada',
    'fecha de publicacion':'fecha en la que se publico la cancion ',
    'artista':'artista que creo la cancion  ',
    'duracion':'tiempo que dura la cancion ' 
}

def ingresar_can():
    can=(input('ingrese cancion: '))
    fec=(input('ingrese la fecha de publicacion: '))
    art=(input('ingrese el artista: '))
    dur=(input('ingrese la duracion de la cancion: '))
    spotify.update({'cancion':can})
    spotify.update({'fecha de publicacion':fec})
    spotify.update({'artista':art})
    spotify.update({'duracion':dur})
    #return cancion
    #restun de arriba cancelado 


ingresar_can()

print (spotify)
#spotify funcion corregida

def listafav():
    fav=(input('¿desea agregar una cancion a la lista de favoritos s/n? '))
    if fav == 'n':
     print('a seleccionado n por lo tanto no desea agregar una cancion ' )
    elif fav == 's':
         fav1=(input(' ingrese la cancion que desea agregar '))
    spotify.update({fav1})
    return fav 

listafav()

print(spotify)

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
        