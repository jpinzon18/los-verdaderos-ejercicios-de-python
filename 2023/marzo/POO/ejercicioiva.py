class producto:

    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio


    def getnombre(self):
        return self.__nombre

    def setnombre(self,nombre):
        self.__nombre=nombre

    def getprecio(self):
        return  self.__precio

    def setprecio(self,precio):
        self.__precio=precio

    def calculadoraiva(self):
          iva=self.__precio*0.19
          return iva

try:
  pro=producto('frijol',3200)
  print('el producto:',pro.getnombre())
  print('cuesta:',pro.getprecio(),'pesos colombianos')
  print('y el iva del producto es: ',pro.calculadoraiva(),'pesos colombianos')
except TypeError:
    print ("no ingreso un tipo de dato soportado")

'''def iva():
   try:
     product=input("ingrese el producto que desea comprar: ")
     price=(int(input("ingrese el precio: ")))
     ivatot=(price*19)
     ivatot2=(ivatot/100)
     print("el producto ingresado es: ",product,"y el precio del mismo es :",price,"y el iva del producto es:  ",ivatot2)
     iva()
   except ValueError:
         print("!no ingreso un numero¡ ")


iva()'''

