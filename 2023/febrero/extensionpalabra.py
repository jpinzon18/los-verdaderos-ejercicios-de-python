<<<<<<< HEAD
def extension():
    pal1=input("ingrese la palabra en español : ")
    lst=[]
    
    for i in range(len(pal1)):
        lst.append(pal1[i])
    contador=(len(lst))
    
    if contador == 0:
        print("no ingresaste una palabra valida vuelve a intentarlo")
    elif contador== 1:
        print("no ingresaste una palabra valida vuelve a intentarlo")
    else:
        print("la palabra ingresada tiene",len(lst),'letras')






=======
def extension():
    pal1=input("ingrese la palabra en español : ")
    lst=[]
    
    for i in range(len(pal1)):
        lst.append(pal1[i])
    contador=(len(lst))
    
    if contador == 0:
        print("no ingresaste una palabra valida vuelve a intentarlo")
    elif contador== 1:
        print("no ingresaste una palabra valida vuelve a intentarlo")
    else:
        print("la palabra ingresada tiene",len(lst),'letras')






>>>>>>> fca79ac4c5c9cbb26d14dad51e2d3152691adb12
extension()