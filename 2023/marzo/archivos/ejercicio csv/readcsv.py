import csv
def oscar_male():
 with open('D:\ejercicios pyhton adso/2023\marzo/archivos\ejercicio csv\oscar_age_male.csv') as csvDataFile:
 #with open('files/people.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    #print(csvReader)
    for row in csvReader:
        #print(row)
        print('index:',row[0])
        print('año:',row[1])
        print('edad:',row[2])
        print('nombre:',row[3])
        print('pelicula',row[4])


def oscar_female():
 with open('D:\ejercicios pyhton adso/2023\marzo/archivos\ejercicio csv\oscar_age_female.csv') as csvDataFile:
 #with open('files/people.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    #print(csvReader)
    for row in csvReader:
        #print(row)
        print('index:',row[0])
        print('año:',row[1])
        print('edad:',row[2])
        print('nombre:',row[3])
        print('pelicula',row[4])

def menu():
 menu1=print("oprima 1 si quiere ver los ganadores")
 menu2=print("oprima 2 si quiere ver las ganadoras")
 try:
     select=int(input("seleccione la opcion que desea usar: "))

     if select == 1:
         oscar_male()
     elif select == 2:
         oscar_female()
 except:
     print("la opcion que selecciono no esta reinicie el programa")

 menu()


menu()