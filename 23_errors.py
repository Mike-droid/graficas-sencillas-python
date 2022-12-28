try:
    print(0/0)
    assert 1 != 1, '1 es diferente de 1 :O'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)


print('hola')
print('hello')