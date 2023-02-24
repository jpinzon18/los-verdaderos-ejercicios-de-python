#en primera instancia el programa sin raise no daria pie a la excepcion por ello en vez de simplemente poner el except el error y cerrarlo con ello se
#coloca la e como una especie de variable para el funcionamiento de la excepcion por ello se imprime "e" aunque cabe aclarar que sin el print de "e"
#la excepcion funcionaria de igual manera,lo anterior es aplicable para ambos.

#PRIMER EJERCICIO:
try:
    #print(1/1))
    raise SyntaxError
except SyntaxError as e:
    print(e)
    print('Cierra el parentesis')

#SEGUNDO EJERCICIO:
try:
    #raise ZeroDivisionError
    print(1/0)
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:
    #print(zde)
    print('prueba error')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#Al estar en values 2 valores en este caso 1 y 0 el asteristo sirve para dividirles 
#por lo tanto en los print hay una "f" debido a que esta permite intercalar tanto texto como numeros
#despues de la excepcion la cual incluye dos en este caso zerodivisionerror y type error nuevamente con e como una especie de variable 
#pero en este caso la salida del except el print viene con type que incluira ademas de "e" la cual ya mencionames permite que en la erminal aparezca el  error
#sin embargo el type que acompaña a "e" tiene la funcion de que ademas de una descripcion vaga como podia ser el None de la excepcion anterior
#aparzeca  valga la redundancia el tipo de error como se muestra en la salida.
#<class 'ZeroDivisionError'> integer division or modulo by zero


#TERCER EJERCICIO:
values = (1, 0)
#x,y=10,12
#print(divmod(10,3))
try:
    q, r = divmod(*values)
    #print('valor de q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#aqui hay una peculiaridad luego de detreminar paraemtrso en la funcion deberia ser una funcion simple pero luego del except
#se  encuentra un else esto esta hecho de manera que sino se cumple la excepcion se ejecute lo que normalmente se ejecutaria dicho de otra
#forma la excepcion va antes del print de resultados en vez de ser la misma excepcion la que de alguna forma "cerrara" el programa.

#CUARTO EJERCICIO
def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 'a'))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Aqui se vuelve a usar la "e" para la excepcion  y "f" para intercalar valores numericos y letras ademas algo extraño por asi decirlo
#la misma funcion en este caso edad es invocada dentro de la misma in esta al tener int se repetira indefinidamente a menos que el usuario ingrese 
#numeros aceptados por int 

#QUINTO EJERCICIO:
def edad():
    try:
        tuedad=int(input("introduce tu edad"))
        print(f'tu edad es  {tuedad}')
        #print('Tu edad es ',tuedad)
    except ValueError as e:    
        print(e)
        print("La edad debe ser un valor numerico...")
        edad()
    
edad()
