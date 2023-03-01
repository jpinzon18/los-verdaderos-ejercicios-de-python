#en este caso s define una clase persona con dos por asi decirlo parametros para luego definir un constructor identificable por las palabras
#__init__ y self en el caso de los parametros, esta ultima define a nombre y el proceso se repetira con las funciones de la clase (getnombre,setnombre)
#luego hay una variable llamada "ob" al tener persona toma el valor e ingresa como parametro el nombre en este caso Maria,despues un print con ob el
#nombre de la variable y el nombre de una de las funciones en el caso del primer print  getnombre que trabajara con el parametro de la variable es decir.
#el nombre maria el proceso se reitera con las otras funciones de la clase y por ultimo un print con type que sencillamente imprime el typo de dato de una variable
#ob en este caso por lo tanto la salida en la terminal deberia ser class__main__persona.
#luego en la clase aprendiz se hace uso de la clase persona vista como paramentro  para luwgo repetir el proceso de obb es decir crear una variable para
#hacer uso de las funciones de la clase en este caso la variable tiene el nombre de app.
class Persona:
    def __init__(self,nombre):
        self.__nombre=nombre
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
print(type(ob))

class Aprendiz(Persona):
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('Pedro',12345)
print(app.getNombre())

