with open('text.txt', 'w+') as file:
    for line in file:
        print(line)

    file.write('\nnuevas cosas en este archivo')
    file.write('\notra linea')
    file.write('\nanuma')
