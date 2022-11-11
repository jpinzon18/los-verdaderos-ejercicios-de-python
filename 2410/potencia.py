x=int(input('ingrese la base : '))
y=int(input('ingrese el exponente'))
i=1
potent=x
while(i<y):
    i+=1
    potent*=x
if y<=0:
    potent=1
print(potent)
        
