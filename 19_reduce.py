import functools

numbers = [5, 4, 3, 2, 1]

"""def accum(counter, item):
    print(f'counter -> {counter}')
    print(f'item -> {item}')
    return counter + item"""

result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)
