def sumatoria_con_rango(minimo:int, maximo:int)-> int:
    sumatoria = 0
    for x in range(minimo, maximo):
        sumatoria += x

    return sumatoria


print(sumatoria_con_rango(20, 30))