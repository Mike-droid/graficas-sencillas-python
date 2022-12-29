import csv
import re

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


def population_by_country(country):
    data = read_csv('./world_population.csv')
    year_population = {}
    for dictionary in data:
        for key in dictionary:
            if dictionary['Country/Territory'] == country:
                if re.search('^\d{4}', key):
                    year_population.setdefault(key[:4], int(dictionary[key]))
    return year_population


if __name__ == '__main__':
    print(population_by_country('Mexico'))

