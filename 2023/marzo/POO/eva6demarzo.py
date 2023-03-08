
class lector:
    def __init__(self,nombre,direccion,telefono):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono

    def getnombre(self):
        return self.__nombre

    def setnombre(self,nombre):
        self.__nombre=nombre

    def getdireccion(self):
        return self.__direccion

    def setdireccion(self,direccion):
        self.__direccion=direccion

    def gettelefono(self):
        return self.__telefono

    def settelefono(self,telefono):
        self.__telefono=telefono

class pedido:

    def __init__(self,id,titulo,codigo):
        self.__id=id
        self.__titulo=titulo
        self.__codigo=codigo

    def getid(self):
        return self.__id

    def setid(self,id):
        self.__id=id

    def gettitulo(self):
        return self.__titulo

    def settitulo(self,titulo):
        self.__titulo=titulo

    def getcodigo(self):
        return self.__codigo

    def setcodigo(self,codigo):
        self.__codigo=codigo

class Bibliotecario:
    def __init__(self,idb):
        self.__idb=idb

    def getidb(self):
        return self.__idb

    def setidb(self,idb):
        self.__idb=idb

class Libro:
    def __init__(self,titulol,tipo,autor,editorial):
        self.__titulol=titulol
        self.__tipo=tipo
        self.__autor=autor
        self.__editorial=editorial

    def gettitulol(self):
        return self.__titulol

    def settitulol(self,titulol):
        self.__titulol=titulol

    def gettipo(self):
        return self.__tipo

    def settipo(self,tipo):
        self.__tipo=tipo

    def getautor(self):
        return self.__autor

    def setautor(self,autor):
        self.__autor=autor

    def geteditorial(self):
        return self.__editorial

    def seteditoorial(self,editorial):
        self.__editorial=editorial

class revista:
    def __init__(self,titulor,tipor,autor,edicion):
        self.__titulor=titulor
        self.__tipor=tipor
        self.__autor=autor
        self.__edicion=edicion

    def gettitulor(self):
        return self.__titulor

    def setitulor(self,titulor):
        self.__titulor=titulor

    def gettipor(self):
        return self.__tipor

    def settipor(self,tipor):
        self.__tipor=tipor

    def getautor(self):
        return self.__autor

    def setauator(self,autor):
        self.__autor=autor

    def getedicion(self):
        return self.__edicion

    def setedicion(self,edicion):
        self.__edicion=edicion

class  estudiante:
    def __init__(self,codigoest):
        self.codigoest=codigoest

    def getcodigoest(self):
        return self.__codigoest

    def setcodigoest(self,codigoest):
        self.__codigoest=codigoest


class docente:
    def __init__(self,codigodoc):
        self.__codigodoc=codigodoc

    def getcodigodoc(self):
        return self.__codigodoc

    def setcodigodoc(self,codigodoc):
        self.__codigodoc=codigodoc

print("presione 1 para ver la informacion del lector")
print("presione 2 para ver la informacion del pedido")
print("presione 3 para ver la informacion del bibliotecario")
print("presione 4 para ver la informacion del libro")
print("presione 5 para ver la informacion del usuario del pedido de la revista")
print("presione 6 para ver la informacion del pedido de revista")
print("presione 7 para ver el tipo y la edicion de la revista")

try:
 intro=int(input("ingrese el numero de la opcion que desea usar: "))

 if intro == 1:
     lec=lector('alavaro','bucaramanga',451262)
     print('el usuario :', lec.getnombre())
     print('que vive en :', lec.getdireccion())
     print('cuyo telefono es: ', lec.gettelefono())
 elif intro == 2:
     lec2=pedido(1512232,'dune',984375847)
     print('con el id: ',lec2.getid())
     print('pidio el libro: ',lec2.gettitulo(),'Que tiene el codigo: ', lec2.getcodigo())
 if intro == 3:
     lec3=Bibliotecario(477847)
     print('la id de el bibliotecario es: ',lec3.getidb())
 elif intro == 4:
     lec4=Libro('dune','ciencia ficcion','frank herbert','de bolsillo')
     print('el titulo del libro es: ',lec4.gettitulol())
     print('cuyo tipo es: ', lec4.gettipo())
     print('el autor es: ',lec4.getautor())
     print('la editorial es: ',lec4.geteditorial())
 if intro == 5:
     lec5=lector('alvaro','bucaramanga',37483738)
     print('el usuario: ',lec5.getnombre())
     print('que vive en :', lec5.getdireccion())
     print('cuyo telefono es: ', lec5.gettelefono())
 if intro == 6:
     lec6=pedido(4785784,'nintendo power',86657798)
     print('con el id: ',lec6.getid())
     print('pidio la revista : ',lec6.gettitulo(),'Que tiene el codigo: ', lec6.getcodigo())
 if intro == 7:
     lec7=revista('nintendo power','revistas de videjuegos','jh ','edicion numero 1')
     print('la revista es: ',lec7.gettitulor())
     print('el tipo es: ',lec7.gettipor())
     print('en la edicion: ',lec7.getedicion())
except ValueError:
    print("la opcion que selecciono no esta disponible reinicie el programa")
