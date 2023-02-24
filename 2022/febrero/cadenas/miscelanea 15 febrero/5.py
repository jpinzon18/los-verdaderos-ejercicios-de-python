
def known():
    try:
     v=input("ingrese la palabra: ")
     if(v[-1]==chr(225)or v[-1]==chr(223)or v[-1]==(237)or v[-1]==chr(243)or v[-1]==chr(250)or v[-1]==chr(193)or v[-1]==chr(201)or v[-1]==chr(205)or v[-1]==chr(211)or v[-1]==chr(218)):
        print("La palabra ingresada es aguda")

     if(v[-2]==chr(225)or v[-2]==chr(223)or v[-2]==(237)or v[-2]==chr(243)or v[-2]==chr(250)or v[-2]==chr(193)or v[-2]==chr(201)or v[-2]==chr(205)or v[-2]==chr(211)or v[-2]==chr(218)):
        print("La palabra ingresada  es grave")
    
     if(v[-3]==chr(225)or v[-3]==chr(223)or v[-3]==(237)or v[-3]==chr(243)or v[-3]==chr(250)or v[-3]==chr(193)or v[-3]==chr(201)or v[-3]==chr(205)or v[-3]==chr(211)or v[-3]==chr(218)):
        print("La palabra ingresada es esdrujula")
     
     if(v[-1]==chr(225)or v[-4]==chr(223)or v[-4]==(237)or v[-4]==chr(243)or v[-4]==chr(250)or v[-4]==chr(193)or v[-4]==chr(201)or v[-4]==chr(205)or v[-4]==chr(211)or v[-4]==chr(218)):
        print("La palabra ingresada es sobreesdrujula")
    except:
        print("la palabra ingresada no esta soportada")

known()