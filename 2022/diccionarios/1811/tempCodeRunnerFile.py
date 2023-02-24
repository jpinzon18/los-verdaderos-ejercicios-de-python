cancion={}
 

def ingresar_can():
    can=(input('ingrese cancion'))
    fecha=(input('ingrese la fecha de publicacion'))
    cancion.update({can,fecha})
    return cancion 


ingresar_can()

print (cancion)