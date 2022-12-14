extra_hours = {}

while True:
    name = input("Ingresa el nombre del empleado: ")
    if name == '':
        break
    
    score = int(input("Ingresa las horas extra trabajadas (0-10): "))
    if score not in range(0, 11):
	    break
    score*=5208
    
    if name in extra_hours:
        extra_hours[name] += (score,)
    else:
        extra_hours[name] = (score,)
print (extra_hours)    
for name in sorted(extra_hours.keys()):
    adding = 0
    counter = 0
    for score in extra_hours[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

