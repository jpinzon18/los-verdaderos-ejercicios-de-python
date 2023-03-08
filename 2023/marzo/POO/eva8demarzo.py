class usuarios:
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

class lector(usuarios):
     def __init__(self,nombre,direccion,telefono,idlec):
        usuarios.__init__(self,nombre,direccion,telefono)
        self.__idlec=idlec

     def getidlec(self):
         return self.__idlec

     def setidlec(self,idlec):
         self.__idlec=idlec

class Bibliotecario(usuarios):
    def __init__(self,nombre,direccion,telefono,idb):
       usuarios.__init__(self,nombre,direccion,telefono)
       self.__idb=idb

    def getidb(self):
        return self.__idb

    def setidb(self,idb):
        self.__idb=idb

class  estudiante(lector):
    def __init__(self,nombre,direccion,telefono,codigoest):
        usuarios.__init__(self,nombre,direccion,telefono)
        self.codigoest=codigoest

    def getcodigoest(self):
        return self.__codigoest

    def setcodigoest(self,codigoest):
        self.__codigoest=codigoest

class docente(lector):
    def __init__(self,nombre,direccion,telefono,idlec,codigodoc):
        lector.__init__(self,nombre,direccion,telefono,idlec)
        self.__codigodoc=codigodoc

    def getcodigodoc(self):
        return self.__codigodoc

    def setcodigodoc(self,codigodoc):
        self.__codigodoc=codigodoc

class material:
    def __init__(self,titulo,tipo):
        self.__titulo=titulo
        self.__tipo=tipo

    def gettitulo(self):
        return self.__titulo

    def settitulo(self,titulo):
        self.__titulo=titulo
    
    def gettipo(self):
        return self.__tipo
    
    def settipo(self,tipo):
        self.__tipo=tipo


class Libro(material):
    def __init__(self,titulo,tipo,autorlibro,editorial):
        material.__init__(self,titulo,tipo)
        self.__autorlibro=autorlibro
        self.__editorial=editorial

    def getautor(self):
        return self.__autorlibro

    def setautor(self,autorlibro):
        self.__autorlibro=autorlibro

    def geteditorial(self):
        return self.__editorial

    def seteditoorial(self,editorial):
        self.__editorial=editorial

class revista(material):
    def __init__(self,titulo,tipo,autorev,edicion):
        material.__init__(self,titulo,tipo)
        self.__autorev=autorev
        self.__edicion=edicion

    def getautorev(self):
        return self.__autorev

    def setauatorev(self,autorev):
        self.__autorev=autorev

    def getedicion(self):
        return self.__edicion

    def setedicion(self,edicion):
        self.__edicion=edicion

class pedido(Libro,revista,Bibliotecario,lector):
    def __init__(self,titulo,tipo,autorlibro,editorial,autorev, edicion,nombre,direccion,telefono,idb,idlec,id,titulope,codigo):
        Libro.__init__(self,titulo,tipo,autorlibro,editorial)
        revista.__init__(self,titulo,tipo,autorev,edicion)
        Bibliotecario.__init__(self,nombre,direccion,telefono,idb)
        lector.__init__(self,nombre,direccion,telefono,idlec)
        self.__id=id
        self.__titulope=titulope
        self.__codigo=codigo

    def getid(self):
        return self.__id

    def setid(self,id):
        self.__id=id

    def gettitulo(self):
        return self.__titulope

    def settitulo(self,titulope):
        self.__titulope=titulope

    def getcodigo(self):
        return self.__codigo

    def setcodigo(self,codigo):
        self.__codigo=codigo


lec=pedido('dune','ciencia ficcion','de boslsillo',9858958)
print('el usuario: ',lec.getnombre(),'con el numero de telefono: ',lec.gettelefono())
print('que vive en la direccion:',lec.getdireccion())
print('identificado con el id: ',lec.getidlec())

