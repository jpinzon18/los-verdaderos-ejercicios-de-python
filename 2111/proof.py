
artista={
    'artista':'a'
}


def ingresar_art():
    art=(input('ingrese el nombre del artista ') )
    artista.update({'artista':art})
    
    
    
    
ingresar_art()

print(artista)    
