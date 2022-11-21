cancion={}
 

def ingresar_can():
    can=(input('ingrese cancion'))
    fecha=(input('ingrese la fecha de publicacion'))
    cancion.update({can,fecha})
    return cancion 


ingresar_can()

print (cancion)


artista={}


def ingresar_art(artista):
    art=(input('ingrese al artista'))
    artista.update({art})
    return artista


ingresar_art(artista)

print(artista)
 

