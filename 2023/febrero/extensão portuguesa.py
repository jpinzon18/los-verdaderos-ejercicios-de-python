def Portuguese():
    palavra=input("digite a palavra em portugues: ")
    pronto=[]

    for i in range(len(palavra)):
        pronto.append(palavra[i])
    contador=(len(palavra))

    if contador == 0:
        print("Você não digitou uma palavra válida, tente novamente")
    elif contador== 1:
        print("Você não digitou uma palavra válida, tente novamente")
    else:
        print("a palavra digitada tem",len(pronto),'cartas')


Portuguese()














































































































































































































































































