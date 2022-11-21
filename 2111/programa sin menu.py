# ejercicio de spotify continuado el 21 de noviembre juan E Pinzon
spotify={
    'cancion':'nombre de la cancion',
    'fecha de publicacion':'fecha de publicacion de la cancion',
    'artista':'artisa de la cancion ingresada',
    'duracion':'duracion de la cancion ingresada' 
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
    fav=(input('¿desea agregar una cancion a la lista de favoritos si/no? '))
    if fav == 'no':
     print('a seleccionado n por lo tanto no desea agregar una cancion ' )
    elif fav == 'si':
         fav1=(input(' ingrese la cancion que desea agregar '))
    spotify.update({fav1})
    

listafav()

print(spotify)