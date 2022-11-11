for c1 in range (1, 500+1):
    for c2 in range (1,500+1):
        for h in range (1, 500+1):
            c=c1**2+c2**2
            h**=2
            if c==h:
                print('c1:',c1,'c2:',c2,'h:',h,'es una terna pitagorica')
                
              