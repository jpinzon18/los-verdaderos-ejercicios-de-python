def division():
    try:
      num1=int(input('ingrese el primer numero'))
      num2=int(input('ingrse el segundo numero'))
      div=(num1/num2)
      print(div)
    except ZeroDivisionError:
        print('error en la division ejecute el programa de nuevo')

division()     