artista={''}


def ingresar_art(artista):
    art=(input('ingrese al artista'))
    artista.update({art})
    return artista


print(ingresar_art(artista))

print(artista)