diccionario={'palabra1':'pal'}

def relleno():
    pal1=(input('ingrese el elemneto que desea agregar al diccionario: '))
    diccionario.update({'palabra1':pal1})
    print(diccionario)


relleno()