"""numbers = []

for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [number * 2 for number in range(1,11)]
print(numbers_v2)"""

"""even_numbers = [number for number in range(1,101) if number % 2 == 0]
print(even_numbers)"""

"""my_dict = {}
for i in range(1,11):
    my_dict[i] = i * 3

print(my_dict)"""

"""my_dict_v2 = { i: i * 3 for i in range(1,11) }
print(my_dict_v2)
"""

"""import random
countries = ['mexico', 'usa', 'canada']
population = { country: random.randint(5,1000) for country in countries }
print(f'full population {population}')

high_population = { country: pop for (country, pop) in population.items() if pop > 700 }
print(f'high population {high_population}')

text = 'hola soy Miguel'
vowels = { character: character.upper() for character in text if character in 'aeiou'}
print(vowels)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

names_and_ages = { name: age for (name, age) in zip(names, ages) }
print(names_and_ages)"""

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [number for number in numbers if number % 2 == 0]

print('v2 =>', even_numbers_v2)