class Persona:
    def __init__(self,nombre,number):
        self.__nombre=nombre
        self.__number=number
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getnumber(self,number):
        return self.__number
    
    def setnumber(self,number):
        self.__number=number


ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
ob.setnumber(345546)
print(ob.getnumber())
#print(type(ob))

#class Aprendiz(Persona):
#        Persona.__init__(self,nombre)
#        self.__ficha=ficha

#    def getFicha(self):
#        return self.__ficha

#app=Aprendiz('Pedro',12345)
###print(app.getNombre())
