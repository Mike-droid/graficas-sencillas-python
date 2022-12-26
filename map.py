numbers = [5, 10, 15, 20, 25]
numbers_double_values = list(map(lambda number: number * 2, numbers))

print(numbers_double_values)

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

print(numbers_1)
print(numbers_2)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result) # [6,8,10] el último elemento no fue tomado en cuenta
