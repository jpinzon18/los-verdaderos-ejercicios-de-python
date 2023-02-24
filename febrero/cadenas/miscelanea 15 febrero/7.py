def es_consonant(letra):
    return letra in "p q b t d c ch j k g f v s z m n ñ l x r w y"

cadena = input("ingrese la cadena:")
cadena_minuscula = cadena.lower()
cantidad_consonantes = 0
for letra in cadena_minuscula:
    if letra.isalpha() and not es_consonant(letra):
        cantidad_consonantes += 1
print(f"En la cadena '{cadena}' hay {cantidad_consonantes} consonantes")

def es_vocal(letra):
    return letra in "aeiou"

mincadena=cadena.lower()
cantidad_vocales=0
for letra in mincadena:
    if letra.isalpha() and not es_vocal(letra):
        cantidad_vocales +=1
print(f"en la cadena'{cadena}'hay {cantidad_vocales} vocales")

def til_vocal(letra):
    return letra in "áéíóú"

tilcadena=cadena.lower()
cantidad_tildes=0
for letra in tilcadena:
    if letra.isalpha() and not til_vocal(letra):
        cantidad_tildes +=1
print(f"en la cadena'{cadena}'hay {cantidad_tildes} vocales con tilde ")


