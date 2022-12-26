items = [
    {
        'product': 'camisa',
        'price': 100,
    },
    {
        'product': 'pantalones',
        'price': 300,
    },
{
        'product': 'tennis',
        'price': 500,
    },
]

prices = list(map(lambda item: item['price'], items))
print(prices)

"""def add_taxes(item):
copy = item.copy()
    copy['taxes'] = copy['price'] * 0.19
    return copy


new_items = list(map(add_taxes, items))
print(new_items)

print(f'items -> {items}')"""

new_items = list(map(lambda item: item | {'tax': item['price'] * .19}, items)) # gracias a '|' no modificamos el array original
print(new_items)
print(items)