#Herencia: ¿por qué y cómo?
#Cuando Python necesita que alguna clase u objeto deba ser presentado como una cadena (es recomendable colocar el objeto como
#argumento en la invocación de la función print()), intenta invocar un método llamado __str__() del objeto y emplear la cadena que devuelve.
#El método por default __str__() devuelve la cadena anterior: fea y poco informativa. Puedes cambiarlo definiendo tu propio método.

'''class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' en ' + self.galaxy


sun = Star("Sol", "Vía Láctea")
print(sun)'''

#El método nuevo __str__() genera una cadena que
#consiste en los nombres de la estrella y la galaxia, nada especial, pero los resultados de impresión se ven mejor ahora, ¿no?

#La herencia es una práctica común (en la programación de objetos) de pasar atributos y métodos de la superclase (definida y existente) a una clase recién creada, llamada subclase.

#En otras palabras, la herencia es una forma de construir una nueva clase, no desde cero, sino utilizando un repertorio de rasgos ya definido.
# La nueva clase hereda (y esta es la clave)
#todo el equipamiento ya existente, pero puedes agregar algo nuevo si es necesario.
#Gracias a eso, es posible construir clases más especializadas (más concretas) utilizando algunos conjuntos de reglas y comportamientos generales predefinidos.

#El factor más importante del proceso es la relación entre la superclase y todas sus subclases (nota: si B es una subclase de A y C es una subclase de B, esto también significa que C es una subclase de A, ya que la relación es totalmente transitiva).

#Aquí se presenta un ejemplo muy simple de herencia de dos niveles:

'''class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass'''


#Podemos decir que:

#La clase Vehicle es la superclase para clases LandVehicle y TrackedVehicle.
#La clase LandVehicle es una subclase de Vehicle y la superclase de TrackedVehicle al mismo tiempo.
#La clase TrackedVehicle es una subclase tanto de Vehicle y LandVehicle.

#Herencia: issubclass()
#Python ofrece una función que es capaz de identificar una relación entre dos clases, y aunque su diagnóstico no es complejo,
# puede verificar si una clase particular es una subclase de cualquier otra clase.

#Así es como se ve:
'''issubclass(ClassOne, ClassTwo)'''

#La función devuelve True si ClassOne es una subclase de ClassTwo, y False de lo contrario.

#EJEMPLO:
'''class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()'''

#Ejecuta el código. El programa produce el siguiente resultado:

''' True	False	False
    True	True	False
    True	True	True '''

#Herencia: isinstance()
#Como ya sabes, un objeto es la encarnación de una clase. Esto significa que el objeto es como un pastel horneado usando una receta que se incluye dentro de la clase.

#Esto puede generar algunos problemas.

#Supongamos que tienes un pastel (por ejemplo, resultado de un argumento pasado a tu función). Deseas saber que receta se ha utilizado para prepararlo. ¿Por qué? Porque deseas saber que esperar de él, por ejemplo, si contiene nueces o no, lo cual es información crucial para ciertas personas.

#Del mismo modo, puede ser crucial si el objeto tiene (o no tiene) ciertas características. En otras palabras, si es un objeto de cierta clase o no.

#Tal hecho podría ser detectado por la función llamada isinstance():

'''isinstance(objectName, ClassName)'''

#La función devuelve True si el objeto es una instancia de la clase, o False de lo contrario.

#Ser una instancia de una clase significa que el objeto (el pastel) se ha preparado utilizando una receta contenida en la clase o en una de sus superclases.

#No lo olvides: si una subclase contiene al menos las mismas características que cualquiera de sus superclases,
#significa que los objetos de la subclase pueden hacer lo mismo que los objetos derivados de la superclase,
#por lo tanto, es una instancia de su clase de inicio y cualquiera de sus superclases.

'''class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
'''

#Esto es lo que obtenemos:

''' True 	False	False	
   True 	True	False	
    True	True	True'''	

#Herencia: el operador is
#También existe un operador de Python que vale la pena mencionar, ya que se refiere directamente a los objetos: aquí está:

'''object_one is object_two'''

#El operador is verifica si dos variables, en este caso (object_one y object_two) se refieren al mismo objeto.
#No olvides que las variables no almacenan los objetos en sí, sino solo los identificadores que apuntan a la memoria interna de Python.

#Asignar un valor de una variable de objeto a otra variable no copia el objeto, sino solo su identificador.
#Es por ello que un operador como is puede ser muy útil en ciertas circunstancias.

'''class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2)
'''

#El código imprime:

'''False
False
True
1 2 1
True False'''

#Existe una clase muy simple equipada con un constructor simple, que crea una sola propiedad. La clase se usa para instanciar dos objetos.
# El primero se asigna a otra variable, y su propiedad val se incrementa en uno.
#Luego, el operador is se aplica tres veces para verificar todos los pares de objetos posibles,
# y todos los valores de la propiedad val son mostrados en pantalla.
#La última parte del código lleva a cabo otro experimento. Después de tres tareas, ambas cadenas contienen los mismos textos,
# pero estos textos se almacenan en diferentes objetos.

#Los resultados prueban que object_1 y object_3 son en realidad los mismos objetos, mientras que string_1 y string_2 no lo son,
#a pesar de que su contenido sea el mismo.

#Cómo Python encuentra propiedades y métodos
#Ahora veremos como Python trata con los métodos de herencia.

'''class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)
'''
#Existe una clase llamada Super, que define su propio constructor utilizado para asignar la propiedad del objeto, llamada name.
#La clase también define el método __str__(), lo que permite que la clase pueda presentar su identidad en forma de texto.
#La clase se usa luego como base para crear una subclase llamadaSub. La clase Sub define su propio constructor, que invoca el de la superclase.
#Toma nota de como lo hemos hecho: Super.__init__(self, name).
#Hemos nombrado explícitamente la superclase y hemos apuntado al método para invocar a __init__(), proporcionando todos los argumentos necesarios.
#Hemos instanciado un objeto de la clase Sub y lo hemos impreso.
#El código da como salida:

'''Mi nombre es Andy.'''

#En el ejemplo anterior, nombramos explícitamente la superclase. En este ejemplo, hacemos uso de la función super(),
# la cual accede a la superclase sin necesidad de conocer su nombre:

'''super().__init__(name)'''

#Nota: puedes usar este mecanismo no solo para invocar al constructor de la superclase,
#pero también para obtener acceso a cualquiera de los recursos disponibles dentro de la superclase.

'''class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
'''
#la salida de este programa es:
'''100 101 102
   200 201 202
   300 301 302'''


#------------------------------------------------------------------------------------------------------------------------------------------------------
#PREGUNTAS:
#¿que es el polimorfismo?
#¿en que consiste la sobreescritura de metodos?
#¿que es una pila contadora?


