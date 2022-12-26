increment = lambda number: number + 1

high_order_function = lambda value, function: value + function(value)

result = high_order_function(5, increment)
# 5 + (5+1)
print(result)
