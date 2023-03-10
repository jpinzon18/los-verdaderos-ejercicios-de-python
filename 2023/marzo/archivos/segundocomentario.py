#se comienza importando de aprendiz todo el contenido y tambien de curso  se prosigue con un input llamado 'nombre'
#luego otro llamado documento el cual solo acepta numeros debido al int, luego otra variable con input la cual es 'ficha
#despues otra variable de nombre "ap" que hara uso de la clase aprendiz que asu vez hara uso de los datos capturados en los inputs
#anteriores.
#en la liena 15 se define otra variable input  "nombrecurso" otra variable horas que solo aceptara numeros debido al int
#y por ultimo c1 que usara la clase curso una vez mas con los datos de los inputs.
#en la linea 20 ap hara uso de la funion "agregarcurso" de la clase aprendiz con los datos de c1
#en la linea 23 con el with haciendo uso de la ruta relativa y la funcion open  comienza el flujo de datos renombrado
#simplemente como flujo,el cual gracias a la funcion write de la linea 25 llenara el archivo aprendices.txt
#haciendo uso de la variable "ap" y las funciones de la clase aprendiz "getficha","getnombre"y "getdocumento" de la
#clase persona a las que en medio de ellas se les adhiere una coma para separarlas unas de otras.
from aprendiz import *
from curso import *

nombre=input('ingrese nombre del aprendiz')
documento=int(input('ingrese documento del aprendiz'))
ficha=input('ingrese ficha del aprendiz')

ap=Aprendiz(ficha,nombre,documento)

nombreCurso=input('ingrese nombre del curso')
horas=int(input('ingrese intensidad horaria del curso'))
c1=Curso(nombreCurso,horas)
ap.agregarCurso(c1)

with open('herencia/aprendices.txt','a') as flujo:
     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')

