import utils

data = [
    {
        'Country': 'México',
        'Population': 500,
    },
    {
        'Country': 'Canada',
        'Population': 300,
    },
    {
        'Country': 'Spain',
        'Population': 700,
    },
]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input('Type the country: ')

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()

