#Archivos: streams
#La apertura del stream no solo está asociada con el archivo,
#sino que también se debe declarar la manera en que se procesará el stream. Esta declaración se llama open mode (modo de apertura).
#Hay dos operaciones básicas a realizar con el stream:

#Lectura del stream: las porciones de los datos se recuperan del archivo y se colocan en un área de memoria administrada por el programa (por ejemplo, una variable).
#Escritura del stream: Las porciones de los datos de la memoria (por ejemplo, una variable) se transfieren al archivo.

#Hay tres modos básicos utilizados para abrir un stream:

#Modo Lectura: un stream abierto en este modo permite solo operaciones de lectura; intentar escribir en la transmisión provocará una excepción (la excepción se llama UnsupportedOperation, 
# la cual hereda el OSError y el ValueError, y proviene del módulo io).
#Modo Escritura: un stream abierto en este modo permite solo operaciones de escritura; intentar leer el stream provocará la excepción mencionada anteriormente.
#Modo Actualizar: un stream abierto en este modo permite tanto lectura como escritura.

''' El stream se comporta casi como una grabadora'''

'''Cuando lees algo de un stream, un cabezal virtual se mueve sobre la transmisión de acuerdo con el número de bytes transferidos desde el stream.

Cuando escribes algo en el stream el mismo cabezal se mueve a lo largo del stream registrando los datos de la memoria.

Siempre que hablemos de leer y escribir en el stream, trata de imaginar esta analogía. 
Los libros de programación se refieren a este mecanismo como la posición actual del archivo, aquí también usaremos este término.'''

#Manejo de archivos
#Python supone que cada archivo está oculto detrás de un objeto de una clase adecuada.

#Un objeto de una clase adecuada es creado cuando abres el archivo y lo aniquilas al momento de cerrarlo.

#Entre estos dos eventos, puedes usar el objeto para especificar que operaciones se deben realizar en un stream en particular.
#Las operaciones que puedes usar están impuestas por la forma en que abriste el archivo.

'''Nota: nunca se utiliza el constructor para dar vida a estos objetos. La unica forma de obtenerlos es invocar la función llamada open().

La función analiza los argumentos proporcionados y crea automáticamente el objeto requerido.

Si deseas deshacerte del objeto, invoca el método denominado close().'''

#Debido al tipo de contenido de los streams, todos se dividen en tipo texto y binario.

#Los streams de texto están estructurados en líneas; es decir,
#contienen caracteres tipográficos (letras, dígitos, signos de puntuación, etc.) dispuestos en filas (líneas),
#como se ve a simple vista cuando se mira el contenido del archivo en el editor.

#Este tipo de archivo es escrito (o leído) principalmente carácter por carácter, o línea por línea.

#Los streams binarios no contienen texto, sino una secuencia de bytes de cualquier valor. Esta secuencia puede ser, por ejemplo, un programa ejecutable, una imagen, un audio o un videoclip, un archivo de base de datos, etc.

#Debido a que estos archivos no contienen líneas, las lecturas y escrituras se relacionan con porciones de datos de cualquier tamaño.
#Por lo tanto, los datos se leen y escriben byte a byte, o bloque a bloque, donde el tamaño del bloque generalmente varía de uno a un valor elegido arbitrariamente.

# AL FINAL DEL CODIGO ESCRITO EN WINDOWS  SE HAYA \r\n LO CUAL HACE QUE EL ARCHIVO SEA INUTIL EN OTOR SISTEMA QUE NO SEA WINDOWS
#ESTO SE LE LLAMA FATLA DE PORTABILIDAD.

#Del mismo modo, el rasgo del programa que permite la ejecución en diferentes entornos se llama portabilidad. Un programa dotado de tal rasgo se llama programa portable.

#Abriendo los streams
'''El abrir un stream se realiza mediante una función que se puede invocar de la siguiente manera:

stream = open(file, mode = 'r', encoding = None)'''


#Vamos a analizarlo:

#El nombre de la función (open) habla por si mismo; si la apertura es exitosa, la función devuelve un objeto stream; de lo contrario, se genera una excepción (por ejemplo, FileNotFoundError si el archivo que vas a leer no existe).

#El primer parámetro de la función (file) especifica el nombre del archivo que se asociará al stream.

#El segundo parámetro (mode) especifica el modo de apertura utilizado para el stream; es una cadena llena de una secuencia de caracteres, y cada uno de ellos tiene su propio significado especial (más detalles pronto).

#El tercer parámetro (encoding) especifica el tipo de codificación (por ejemplo, UTF-8 cuando se trabaja con archivos de texto).

#La apertura debe ser la primera operación realizada en el stream.
#Nota: el modo y los argumentos de codificación pueden omitirse; en dado caso, se tomarán sus valores predeterminados.
#El modo de apertura predeterminado es leer en modo de texto, mientras que la codificación predeterminada depende de la plataforma utilizada. 

'''Modos para abrir los streams
r modo de apertura: lectura

El stream será abierto en modo lectura.
El archivo asociado con el stream debe existir y tiene que ser legible, de lo contrario la función open() generará una excepción.'''


'''w modo de apertura: escritura

El stream será abierto en modo escritura.
El archivo asociado con el stream no necesita existir. Si no existe, se creará; si existe, se truncará a la longitud de cero (se borra);
si la creación no es posible (por ejemplo, debido a permisos del sistema) la función open() generará una excepción.'''


'''a modo de apertura: adjuntar

El stream será abierto en modo adjuntar.
El archivo asociado con el stream no necesita existir; si no existe, se creará; si existe, el cabezal de grabación virtual se establecerá 
al final del archivo (el contenido anterior del archivo permanece intacto).'''

'''r+ modo de apertura: lectura y actualización

El stream será abierto en modo lectura y actualización.
El archivo asociado con el stream debe existir y tiene que permitir escritura, de lo contrario la función open() generará una excepción.
Se permiten operaciones de lectura y escritura en el stream.'''


'''w+ modo de apertura: escritura y actualización

El stream será abierto en modo escritura y actualización.
El archivo asociado con el stream no necesita existir; si no existe, se creará; el contenido anterior del archivo permanece intacto.
Se permiten operaciones de lectura y escritura en el stream.'''

#Seleccionando modo de texto y modo binario
#Si hay una letra b al final de la cadena del modo significa que el stream se debe abrir en el modo binario.

#Si la cadena del modo termina con una letra t el stream es abierto en modo texto.

#El modo texto es el comportamiento predeterminado que se utiliza cuando no se especifica ya sea modo binario o texto.

#Finalmente, la apertura exitosa del archivo establecerá la posición actual del archivo (el cabezal virtual de lectura/escritura) 
#antes del primer byte del archivo si el modo no es a y después del último byte del archivo si el modo es a.


#Modo texto	Modo binario	Descripción
#rt	rb	lectura
#wt	wb	escritura
#at	ab	adjuntar
#r+t	r+b	lectura y actualización
#w+t	w+b	escritura y actualización
#EXTRA

#también puedes abrir un archivo para su creación exclusiva. Puedes hacer esto usando el modo de apertura x. Si el archivo ya existe, la función open() generará una excepción.

#Abriendo el stream por primera vez

#EjEMPLO:

try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # El procesamiento va aquí.
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)

#Cerrando streams
#La última operación realizada en un stream (esto no incluye a los streams stdin, stdout, y stderr pues no lo requieren) debe ser cerrarlo.

#Esa acción se realiza mediante un método invocado desde dentro del objeto del stream: stream.close().

#El nombre de la función es fácil de entender close(), es decir cerrar.
#La función no espera argumentos; el stream no necesita estar abierto.
#La función no devuelve nada pero genera una excepción IOError en caso de un error.
#La mayoría de los desarrolladores creen que la función close() siempre tiene éxito y, por lo tanto, no hay necesidad de verificar si ha realizado su tarea correctamente.

#Diagnosticando problemas con los streams
#El objeto IOError está equipado con una propiedad llamada errno (el nombre viene de la frase error number, número de error) y puedes accederla de la siguiente manera:

'''try:
    # Algunas operaciones con streams.
except IOError as exc:
    print(exc.errno)


El valor del atributo errno se puede comparar con una de las constantes simbólicas predefinidas en módulo errno.'''

'''import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)
'''

#EJEMPLOS:

# Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
stream = open("tzop.txt", "rt", encoding = "utf-8")

# Se imprime el contenido del archivo:
print(stream.read()) 


from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

#Si se aplica a un archivo de texto, la función es capaz de:

#Leer un número determinado de caracteres (incluso solo uno) del archivo y devolverlos como una cadena.
#Leer todo el contenido del archivo y devolverlo como una cadena.
#Si no hay nada más que leer (el cabezal de lectura virtual llega al final del archivo), la función devuelve una cadena vacía.

#Procesando archivos de texto: readline()
#El método intenta leer una línea completa de texto del archivo, y la devuelve como una cadena en caso de éxito. De lo contrario, devuelve una cadena vacía.

from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


#SALIDA:

'''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Caracteres en el archivo: 131
Líneas en el archivo:      4'''

#Procesando archivos de texto: readlines()

#Cuando el método readlines(), se invoca sin argumentos, intenta leer todo el contenido del archivo y devuelve una lista de cadenas, un elemento por línea del archivo.

stream = open("text.txt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()

#SALIDA:

['Beautiful is better than ugly.\n']
['Explicit is better than implicit.\n']
['Simple is better than complex.\n']
['Complex is better than complicated.']

#Manejando archivos de texto: write()

#El método se llama write() y espera solo un argumento: una cadena que se transferirá a un archivo abierto (no lo olvides),
# el modo de apertura debe reflejar la forma en que se transfieren los datos, escribir en un archivo abierto en modo de lectura no tendrá éxito).

from os import strerror

try:
	file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))


'''El código crea un archivo con el siguiente texto:

línea #1
línea #2
línea #3
línea #4
línea #5
línea #6
línea #7
línea #8
línea #9
línea #10'''

#¿Qué es un bytearray?
#Antes de comenzar a hablar sobre archivos binarios, tenemos que informarte sobre una de las clases especializadas que Python usa para almacenar datos amorfos.

#Los datos amorfos son datos que no tienen forma específica, son solo una serie de bytes.

#Python tiene más de un contenedor, uno de ellos es una clase especializada llamada bytearray, como su nombre indica, es un arreglo que contiene bytes (amorfos).

#Si deseas tener dicho contenedor, por ejemplo, para leer una imagen de mapa de bits y procesarla de alguna manera, 
# debes crearlo explícitamente, utilizando uno de los constructores disponibles.

#Observa:

data = bytearray(10)

#Tal invocación crea un objeto bytearray capaz de almacenar diez bytes.

#Bytearrays: continuación
#Bytearrays se asemejan a listas en muchos aspectos. Por ejemplo, son mutables, son susceptibles a la función len(), y puedes acceder a cualquiera de sus elementos
#usando indexación convencional.

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

#Existe una limitación importante: no debes establecer ningún elemento del arreglo de bytes con un valor que no sea un entero
# (violar esta regla causará una excepción TypeError) y tampoco está permitido asignar un valor fuera del rango de 0 a 255 
# (a menos que quieras provocar una excepción ValueError).

'''Nota: hemos utilizado dos métodos para iterar el arreglo de bytes, y hemos utilizado la función hex() para ver los elementos impresos como valores hexadecimales.'''

from os import strerror

data = bytearray(10)  #Primero, inicializamos bytearray con valores a partir de 10

for i in range(len(data)):
    data[i] = 10 + i

try:
    binary_file = open('file.bin', 'wb')                 
    binary_file.write(data)
    binary_file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

# Ingresa aquí el código que lee los bytes del stream.
