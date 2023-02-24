#apuntes hechos por juan esteban pinzon el dia 16 de febrero de 2023 y tomados del curso de cisco netacademy
#El método capitalize()
#El método capitalize() hace exactamente lo que dice - crea una nueva cadena con los caracteres tomados de la cadena fuente, pero intenta modificarlos de la siguiente manera:
#Si el primer carácter dentro de la cadena es una letra (nota: el primer carácter es el elemento con un índice igual a 0, no es el primer carácter visible), se convertirá a mayúsculas.
#Todas las letras restantes de la cadena se convertirán a minúsculas.
#No olvides que:
#La cadena original desde la cual se invoca el método no se cambia de ninguna manera, la inmutabilidad de una cadena debe obedecerse sin reservas.
#La cadena modificada (en mayúscula en este caso) se devuelve como resultado; si no se usa de alguna manera (asígnala a una variable o pásala a una función / método) desaparecerá sin dejar rastro.
#Ejemplo:
## Demostración del método capitalize():
print('aBcD'.capitalize())
#Esto es lo que imprime:
#Abcd

#El método center()
#La variante de un parámetro del método center() genera una copia de la cadena original, tratando de centrarla dentro de un campo de un ancho especificado.
#El centrado se realiza realmente al agregar algunos espacios antes y después de la cadena.
#No esperes que este método demuestre habilidades sofisticadas. Es bastante simple.
#El ejemplo en el editor usa corchetes para mostrar claramente donde comienza y termina realmente la cadena centrada.
#Su salida se ve de la siguiente manera:
# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
#Su salida se ve de la siguiente manera:
#[  alpha   ]

#El método endswith()
#El método endswith() comprueba si la cadena dada termina con el argumento especificado y devuelve True(verdadero) o False(falso), dependiendo del resultado.
#Ejemplo:
# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

#Observa el ejemplo en el editor, analízalo y ejecútalo. Su salida es:
#si

#El método find()
#El método find() es similar al método index(), el cual ya conoces - busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero:

#Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
#Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.
#Analiza el código en el editor. Así es como puedes usarlo.
# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))
#El ejemplo imprime:
1
-1
#Si deseas realizar la búsqueda, no desde el principio de la cadena, sino desde cualquier posición, puedes usar una variante de dos parámetros del método find(). Mira el ejemplo:
print('kappa'.find('a', 2))
#El segundo argumento especifica el índice en el que se iniciará la búsqueda (no tiene que estar dentro de la cadena).
#De las dos letras a, solo se encontrará la segunda. Ejecuta el código y verifica.

#El método isalnum()
#El método sin parámetros llamado isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y devuelve True(verdadero) o False(falso) de acuerdo al resultado.
#Observa el ejemplo en el editor y ejecútalo.
# Demostración del método the isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

#Nota: cualquier elemento de cadena que no sea un dígito o una letra hace que el método regrese False(falso). Una cadena vacía también lo hace.
#El resultado de ejemplo es:

True
True
True
False
False
False

#El método isalpha()
#El método isalpha() es más especializado, se interesa en letras solamente.

# Ejemplo 1: Demostración del método isapha():
print("Moooo".isalpha())
print('Mu40'.isalpha())

#Observa el Ejemplo 1, su salida es:

True
False

#El método isdigit()
#Al contrario, el método isdigit() busca solo dígitos - cualquier otra cosa produce False(falso) como resultado.

# Ejemplo 2: Demostración del método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())

#Observa el Ejemplo 2, su salida es:

True
False

#El método islower()
#El método islower() es una variante de isalpha() - solo acepta letras minúsculas.
# Ejemplo 1: Demostración del método islower():
print("Moooo".islower())
print('moooo'.islower())
#Observa el Ejemplo 1 en el editor, genera:

False
True

#El método isspace()
#El método isspace() identifica espacios en blanco solamente - no tiene en cuenta ningún otro carácter (el resultado es entonces False).
# Ejemplo 2: Demostración del método isspace(:

print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

#Observa el Ejemplo 2 en el editor, genera:

True
True
False

#El método isupper()
#El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.
# Ejemplo 3: Demostración del método isupper():

print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

#De nuevo, observa el Ejemplo 3 en el editor, genera:

False
False
True


#El método join()
#El método join() es algo complicado, así que déjanos guiarte paso a paso:

#Como su nombre lo indica, el método realiza una unión y espera un argumento del tipo lista; se debe asegurar que todos los elementos de la lista sean cadenas: de lo contrario, el método generará una excepción TypeError.
#Todos los elementos de la lista serán unidos en una sola cadena pero...
#... la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
#La cadena recién creada se devuelve como resultado.
#Echa un vistazo al ejemplo en el editor. Vamos a analizarlo:

# Demonstrating the join() method:
print(".".join(["omicron", "pi", "rho"]))


#El método join() se invoca desde una cadena que contiene una coma (la cadena puede ser larga o puede estar vacía).
#El argumento del join es una lista que contiene tres cadenas.
#El método devuelve una nueva cadena.

#Aquí está:
#omicron.pi.rho

#El método lower()
#El método lower() genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas, y devuelve la cadena como resultado. Nuevamente, la cadena original permanece intacta.
#Si la cadena no contiene caracteres en mayúscula, el método devuelve la cadena original.
#Nota: El método lower() no toma ningún parámetro.

# Demostración del método lower():
print("SiGmA=60".lower())

#La salida del ejemplo del editor es:

sigma=60

#Nota:el metodo upper realiza lo contrario pasa de minusculas a mayusculas

#El método lstrip()
#El método sin parámetros lstrip() devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.

#Analiza el ejemplo en el editor.

# Demostración del método the lstrip():
print("[" + " tau ".lstrip() + "]")

#Las salida del ejemplo es:
#[tau ]

#El método con un parámetro lstrip() hace lo mismo que su versión sin parámetros, pero elimina todos los caracteres incluidos en el argumento (una cadena), no solo espacios en blanco:

print("www.cisco.com".lstrip("w."))

#Aquí no se necesitan corchetes, ya que el resultado es el siguiente:
#cisco.com

#El método replace()
#El método replace() con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento.
#Analiza el código en el editor y ejecútalo.

# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

#La salida del ejemplo es:

#www.pythoninstitute.org
#Thare are it!
#Apple

#El método rfind()
#Los métodos de uno, dos y tres parámetros denominados rfind() hacen casi lo mismo que sus contrapartes (las que carecen del prefijo r), pero comienzan sus búsquedas desde el final de la cadena, no el principio (de ahí el prefijo r, de reversa).

#Echa un vistazo al código en el editor e intenta predecir su salida. Ejecuta el código para verificar si tenías razón.

# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#el resultado es:
8
-1
4

#El método rstrip()
#Dos variantes del método rstrip() hacen casi lo mismo que el método lstrip, pero afecta el lado opuesto de la cadena.
#Observa el ejemplo en el editor. ¿Puedes adivinar su salida? Ejecuta el código para verificar tus conjeturas.
# Demostración del método rstrip():

print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

#el resultado sera:
#[ upsilon]
#cis
#Como de costumbre, te recomendamos experimentar con tus propios ejemplos.

#El método split()
#El método split() divide la cadena y crea una lista de todas las subcadenas detectadas.
#El método asume que las subcadenas están delimitadas por espacios en blanco - los espacios no participan en la operación y no se copian en la lista resultante.
#Si la cadena está vacía, la lista resultante también está vacía.

# Demostración del método split():
print("phi       chi\npsi".split())

#Observa el código en el editor. El ejemplo produce el siguiente resultado:

['phi', 'chi', 'psi']

#Nota: la operación inversa se puede realizar por el método join().

#El método startswith()
#El método startswith() es un espejo del método endswith() - comprueba si una cadena dada comienza con la subcadena especificada.

# Demostración del método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

#Observa el ejemplo en el editor. Este es el resultado:

False
True

#El método strip()
#El método strip() combina los efectos causados por rstrip() y lstrip() - crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
#Observa el segundo ejemplo en el editor.
# Demostración del método strip():

print("[" + "   aleph   ".strip() + "]")

# Este es el resultado que devuelve:
#[aleph]

#El método swapcase()
#El método swapcase() crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena original: los caracteres en mayúscula se convierten en minúsculas y viceversa.

#Todos los demás caracteres permanecen intactos.

# Demostración del método swapcase():
print("Yo sé que no sé nada.".swapcase())

print()

#el resultado sera:
#yO SÉ QUE NO SÉ NADA.

#El método title()
#El método title() realiza una función algo similar cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.

#Observa el segundo ejemplo en el editor

# Demostración del método title():
print("Yo sé que no sé nada. Part 1.".title())

print()
#Este es el resultado:
#Yo Sé Que No Sé Nada. Parte 1.

#El método upper()
#Por último, pero no menos importante, el método upper() hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas, y devuelve la cadena como resultado.

#Observa el tercer ejemplo en el editor:
# Demostración del método upper():
print("Yo sé que no sé nada. Part 2.".upper())

#Produce:
#YO SÉ QUE NO SÉ NADA. PARTE 2.
