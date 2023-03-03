#¿Qué es un objeto?
#Una clase (entre otras definiciones) es un conjunto de objetos. Un objeto es un ser perteneciente a una clase.
#Un objeto es una encarnación de los requisitos, rasgos y cualidades asignados a una clase específica.
#Esto puede sonar simple, pero ten en cuenta las siguientes circunstancias importantes. Las clases forman una jerarquía.

#Herencia
#Definamos uno de los conceptos fundamentales de la programación de objetos, llamado herencia. Cualquier objeto vinculado a un nivel específico de una jerarquía de clases hereda todos los rasgos (así como los requisitos y cualidades) definidos dentro de cualquiera de las superclases.
#La clase de inicio del objeto puede definir nuevos rasgos (así como requisitos y cualidades) que serán heredados por cualquiera de sus superclases.

#¿Qué contiene un objeto?
#La programación orientada a objetos supone que cada objeto existente puede estar equipado con tres grupos de atributos:

#Un objeto tiene un nombre que lo identifica de forma exclusiva dentro de su namespace (aunque también puede haber algunos objetos anónimos).
#Un objeto tiene un conjunto de propiedades individuales que lo hacen original, único o sobresaliente (aunque es posible que algunos objetos no tengan propiedades).
#Un objeto tiene un conjunto de habilidades para realizar actividades específicas, capaz de cambiar el objeto en sí, o algunos de los otros objetos.

#EJEMPLO:
#Max es un gato grande que duerme todo el día.

#Nombre del objeto = Max
#Clase = Gato
#Propiedad = Tamaño (Grande)
#Actividad = Dormir (Todo el día)

#Es hora de definir la clase más simple y crear un objeto. Analiza el siguiente ejemplo:

'''class TheSimplestClass:
    pass'''

#La clase recién definida se convierte en una herramienta que puede crear nuevos objetos. La herramienta debe usarse explícitamente, bajo demanda.
#Imagina que deseas crear un objeto (exactamente uno) de la clase TheSimplestClass.
#Para hacer esto, debes asignar una variable para almacenar el objeto recién creado de esa clase y crear un objeto al mismo tiempo.
#Se hace de la siguiente manera:

'''my_first_object = TheSimplestClass()'''

#El acto de crear un objeto de la clase seleccionada también se llama instanciación (ya que el objeto se convierte en una instancia de la clase).
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PUNTOS CLAVE:

##1. Una clase es una idea (más o menos abstracta) que se puede utilizar para crear varias encarnaciones; una encarnación de este tipo se denomina objeto.
#2. Cuando una clase se deriva de otra clase, su relación se denomina herencia. La clase que deriva de la otra clase se denomina subclase.
# El segundo lado de esta relación se denomina superclase.
# Una forma de presentar dicha relación es en un diagrama de herencia, donde:

#Las superclases siempre se presentan encima de sus subclases.
#Las relaciones entre clases se muestran como flechas dirigidas desde la subclase hacia su superclase.

#3. Los objetos están equipados con:

#Un nombre que los identifica y nos permite distinguirlos.
#Un conjunto de propiedades (el conjunto puede estar vacío).
#Un conjunto de métodos (también puede estar vacío).

#4. Para definir una clase de Python,se necesita usar la palabra clave reservada class. Por ejemplo:

'''class This_Is_A_Class:
     pass'''


#5. Para crear un objeto de la clase previamente definida, se necesita usar la clase como si fuera una función. Por ejemplo:

'''this_is_an_object = This_Is_A_Class()'''

#¿Qué es una pila?
#Una pila es una estructura desarrollada para almacenar datos de una manera muy específica. Imagina una pila de monedas. No puedes poner una moneda en ningún otro lugar sino en la parte superior de la pila.

#Del mismo modo, no puedes sacar una moneda de la pila desde ningún lugar que no sea la parte superior de la pila. Si deseas obtener la moneda que se encuentra en la parte inferior, debes eliminar todas las monedas de los niveles superiores.

#El nombre alternativo para una pila (pero solo en la terminología de TI) es UEPS (LIFO son sus siglas en inglés).

#Es una abreviatura para una descripción muy clara del comportamiento de la pila: Último en Entrar - Primero en Salir (Last In - First Out). La moneda que quedó en último lugar en la pila saldrá primero.

#Una pila es un objeto con dos operaciones elementales, denominadas convencionalmente push (cuando un nuevo elemento se coloca en la parte superior) y pop (cuando un elemento existente se retira de la parte superior).

#Las pilas se usan muy a menudo en muchos algoritmos clásicos, y es difícil imaginar la implementación de muchas herramientas ampliamente utilizadas sin el uso de pilas.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#La pila: el enfoque procedimental
#Primero, debes decidir como almacenar los valores que llegarán a la pila.
#Sugerimos utilizar el método más simple, y emplear una lista para esta tarea. 
# Supongamos que el tamaño de la pila no está limitado de ninguna manera. Supongamos también que el último elemento de la lista almacena el elemento superior.

#La pila en sí ya está creada:

stack = []


#Estamos listos para definir una función que coloca un valor en la pila. Aquí están las presuposiciones para ello:

#El nombre para la función es push.
#La función obtiene un parámetro (este es el valor que se debe colocar en la pila).
#La función no retorna nada.
#La función agrega el valor del parámetro al final de la pila.
#Así es como lo hemos hecho, echa un vistazo:

'''def push(val):
    stack.append(val)'''


#Ahora es tiempo de que una función quite un valor de la pila. Así es como puedes hacerlo:

#El nombre de la función es pop.
#La función no obtiene ningún parámetro.
#La función devuelve el valor tomado de la pila.
#La función lee el valor de la parte superior de la pila y lo elimina.
#La función esta aqui:

'''def pop():
    val = stack[-1]
    del stack[-1]
    return val'''


#Nota: la función no verifica si hay algún elemento en la pila.

#Armemos todas las piezas juntas para poner la pila en movimiento. El programa completo empuja (push) tres números a la pila, los saca e imprime sus valores en pantalla. Puedes verlo en la ventana del editor.

#El programa muestra el siguiente texto en pantalla:

#1
#2
#3

'''stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())'''

#La pila, el enfoque orientado a objetos
#Por supuesto, la idea principal sigue siendo la misma. Usaremos una lista como almacenamiento de la pila. Solo tenemos que saber como poner la lista en la clase.

#Comencemos desde el principio: así es como comienza la pila orientada a objetos:

'''class Stack:'''


#Ahora, esperamos dos cosas de la clase:

#Queremos que la clase tenga una propiedad como el almacenamiento de la pila, tenemos que "instalar" una lista dentro de cada objeto de la clase (nota: cada objeto debe tener su propia lista; la lista no debe compartirse entre diferentes pilas).
#Despues, queremos que la lista esté oculta de la vista de los usuarios de la clase.
#¿Cómo se hace esto?

#A diferencia de otros lenguajes de programación, Python no tiene medios para permitirte declarar una propiedad como esa.

#En su lugar, debes agregar una instrucción específica. Las propiedades deben agregarse a la clase manualmente.

#¿Cómo garantizar que dicha actividad tiene lugar cada vez que se crea una nueva pila?

#Existe una manera simple de hacerlo, tienes que equipar a la clase con una función específica:

#Tiene que ser nombrada de forma estricta.
#Se invoca implícitamente cuando se crea el nuevo objeto.
#Dicha función es llamada el constructor, ya que su propósito general es construir un nuevo objeto. 
#El constructor debe saber todo acerca de la estructura del objeto y debe realizar todas las inicializaciones necesarias.

#Agreguemos un constructor muy simple a la nueva clase. Echa un vistazo al código:

'''class Stack:
     def __init__(self):
         print("¡Hola!")


stack_object = Stack()'''


#Expliquemos más a detalle:

#El nombre del constructor es siempre __init__.
#Tiene que tener al menos un parámetro (discutiremos esto más adelante); el parámetro se usa para representar el objeto recién creado: puedes usar el parámetro para manipular
#el objeto y enriquecerlo con las propiedades necesarias; harás uso de esto pronto.
#Nota: el parámetro obligatorio generalmente se denomina self, es solo una sugerencía, pero deberías seguirla, simplifica el proceso de lectura y comprensión de tu código.
#El código está en el editor. Ejecútalo ahora.

#Aquí está su salida:

#¡Hola!

class Stack:  # Definiendo la clase de la pila.
    def __init__(self):  # Definiendo la función del constructor.
        print("¡Hola!")


stack_object = Stack()  # Instanciando el objeto.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

