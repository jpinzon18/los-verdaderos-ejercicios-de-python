'''class Stack:  # Definiendo la clase de la pila.
    def __init__(self):  # Definiendo la función del constructor.
        print("¡Hola!")


stack_object = Stack()  # Instanciando el objeto.'''

'''class Stack:
    def __init__(self):
        self.stack_list = []

stack_object = Stack()
print(len(stack_object.stack_list))'''

#Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__), se vuelve privado, esto significa que solo
# se puede acceder desde dentro de la clase.
#No puedes verlo desde el mundo exterior. Así es como Python implementa el concepto de encapsulación.

'''class Stack:
    def __init__(self):
        self.__stack_list = []

try:
  stack_object = Stack()
  print(len(stack_object.__stack_list))
except AttributeError:
    print("El dato al que desea acceder es privado")'''

class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())



