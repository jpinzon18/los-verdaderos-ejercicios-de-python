import random
vec=[0,1]

def fibonacci(tam):
    tam=round((random.random()*25-10)+10)
    print('tam=',tam)
    for i in range(2,tam):
        vec.append(vec[i-1]+vec[i+2])


print (fibonacci(6))
