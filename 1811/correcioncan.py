# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
ejemplo={
    'cancion':'aaa',
    'fecha':'sfsdfsdfsd'
}
cancion={}
 

def ingresar_can():
    can=(input('ingrese cancion'))
    fec=(input('ingrese la fecha de publicacion'))
    cancion.update({'cancion':can})
    cancion.update({'fecha':fec})
    #return cancion 


ingresar_can()

print (cancion)