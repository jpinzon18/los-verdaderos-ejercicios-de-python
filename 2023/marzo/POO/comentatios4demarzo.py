#como ya es costumbre se define la clase en este caso aprendiz luego un constructor con parametros self y nombre y en este caso tambien incluye una lista "cursos"
#en la linea 13 se encuentra la primera funcion de la clase "agregarcurso"  con el parametro nombre curso  para consecuentemente en la linea 14 ejecutar un append para
#actualizar la lista cursos con el parametro nombrecurso. en la linea  15 se encuentra la funcion vercusros la cual simplemente retorna la lista cursos  ya actualizada. 
#posteriormente en la linea 18 se crea una nueva clase "curso"en este caso la cual como ya es costumbre tiene un constructor con el parametro nombrecurso(visto en la clase aprendiz).
#dentro de la clase hay una funcion getter para nombre curso. en la liena 25  se encuentra ob la cual le da a la clase aprenidz el parametro para nombre en este caso 'miguel.
#c1,c2 y c3 usan la clase curso cada una con diferente nombre del curso para el parametro. para que luego se haga uso tanto de ob como de c1,c2 y c3 con la funcion agregarcurso de la clase aprendiz.
#luego un for en la linea 33 hace uso de  la lista cursos  en la funcion vercursos la cual ya se encuentra con los datos nuevos de la funcion agregarcurso para que imprima tanto la lista cursos.
#como la funcion getnombrecurso.  
class Aprendiz:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[]
    def agregarCurso(self,nombreCurso):
        self.__cursos.append(nombreCurso)
    def verCursos(self):
        return self.__cursos

class Curso:
    def __init__(self,nombreCurso):
        self.__nombreCurso=nombreCurso

    def getNombreCurso(self):
        return self.__nombreCurso
    
ob=Aprendiz('Miguel')
c1=Curso('Python Basico')
c2=Curso('Python Intermedio')
c3=Curso('Java Basico')

ob.agregarCurso(c1)
ob.agregarCurso(c2)
ob.agregarCurso(c3)

for curso in ob.verCursos():
    print(curso.getNombreCurso())

del ob
#print(ob)
print('.....',c1.getNombreCurso())