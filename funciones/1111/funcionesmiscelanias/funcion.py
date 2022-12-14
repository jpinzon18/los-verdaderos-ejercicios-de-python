import random
def parimpar(num):
    if num%2==0:
        print('par')
    else:
        print('impar')

lista=[]
for i in range(10):
    lista.append(round(random.randrange(100)))
    print(lista)
for i in lista:
    print(i)
    parimpar(i)
    
