#se define flujo el cual con open devuelve un stream con la ruta telativa de un archivo en este caso inicio el cual es de
#texto facilmente identificable por la extension ".txt" seguido por una a la cual le permite si el archivo
#no esta creado procede a crearlo y ejecutarse en el mismo posteriormente en  la linea 9 se utiliza la funcion write en flujo.
#la cual pondra en el archivo el texto entre parentesis '\nCuando estudian con juicio' para luego definir "datos" con la cual
#la funcion read lee el archivo que posteriormente se imprime.

flujo=open('archivos/inicio.txt','a')
#datos=flujo.read()
#print(datos)
flujo.write('\nCuando estudian con juicio')
datos=flujo.read()
print(datos)

