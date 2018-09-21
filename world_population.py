"""
Python 3.6
@Author: wrgsRay
"""
import json


def main():
    # load the data into a list.
    filename = 'population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)
    # Print the 2010 population for each country.
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            print(f'{country_name} : {population}')


if __name__ == '__main__':
    main()
