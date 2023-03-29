import sqlite3                                                        #se importa el paquete sqlite3 para la comunicacion entre el codigo de pyhton y la
                                                                      #base de datos
#con=sqlite3.connect('C:\\padilla\\sqlite-tools\\db\\pythondb.db')    ruta absoluta a la base de datos
con=sqlite3.connect('pythonsqlite/pythondb.db')                       #se crea un variable o objeto llamada "con"(abrebiado de conection)con la que
                                                                      #por medio de la ruta(en este caso relativa se especifica cual es la base de datos ) 
                                                                      #que se va a usar.



print(type(con))                                                      #un print sencillo para saber de que typo es la variable "con"   

micursor=con.cursor()                                                 #una nueva variable o objeto qeu hace uso de "con y ahora un metodo llamado cursor" 

print(type(micursor))
new_sql="SELECT * from Persona;"
micursor.execute(new_sql)
lista=micursor.fetchall()
for fila in lista:
    print(fila[0])
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('*'*50)
