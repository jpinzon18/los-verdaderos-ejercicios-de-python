#realize una funcion que permita introducir un cantidad de joules y de segundos  y los convierta a watts 
def jules():
    jul=int(input('ingrese la cantidad en joules: '))
    time=int(input('ingrese el tiempo: '))
    print('los joules ingresados fueron: ',jul, 'y el tiempo: ',time)
    op=(jul/time)
    print('la cantidad de joules ingresada en watts equivale a: ',op)



jules()