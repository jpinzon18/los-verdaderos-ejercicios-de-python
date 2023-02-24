def div():
 try:
     v1=int(input("ingrese el primer digito: "))
     v2=int(input("ingrese el segundo digito: "))
     total=(v1/v2)
     print(total)
 except (ArithmeticError,ValueError):
     print("su division a provocado un aritmetic error por favor reinicie el programa")
 else:
     div()

div()

