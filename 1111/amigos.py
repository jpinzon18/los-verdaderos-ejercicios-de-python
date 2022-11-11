





def divisores(numero):
    suma=0
    for i in range(1,numero):
       if numero%i==0:
          suma+=i
    return suma

def amigos(x,y):
   sumx=divisores(x)
   sumy=divisores(y)
   if x==sumy and y==sumx:
       return 'amigos'
   else:
       return 'not panas' 
   
print(amigos(220,284))



