numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
new_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(new_numbers)
