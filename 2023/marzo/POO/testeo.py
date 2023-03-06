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
        self.tipo=tipo
        self.autor=autor
        self.editorial=editorial
    
    def gettitulol(self):
        return self.__titulol
    
    def settitulol(self,titulol):
        self.__titulol=titulol
    
    def gettipo(self):
        return self.__tipó
    
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
