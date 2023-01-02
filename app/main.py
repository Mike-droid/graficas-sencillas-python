import charts
import pandas as pd

def run():
    df = pd.read_csv('../world_population.csv')
    df = df[df['Continent'] == 'Europe']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values

    charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
    run()

