#file = open('./text.txt')
"""#print(file.read()) # es útil con archivos ligeros
print(file.readline()) # es útil con archivos largos
print(file.readline())
print(file.readline())"""

# usando 'with' nos ahorramos el tener que usar el método 'close'
with open('text.txt') as file:
    for line in file:
        print(line)


#file.close() # libera espacio en memoria