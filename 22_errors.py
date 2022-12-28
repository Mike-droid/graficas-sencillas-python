# print(0/0) # ZeroDivisionError: division by zero

"""suma = lambda x,y: x + y
assert suma(2,2) == 5 # AssertionError"""

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)

