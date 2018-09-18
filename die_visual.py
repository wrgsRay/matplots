"""
Python 3.6
@Author: wrgsRay
"""
from die import Die


def main():
    # Create a D6.
    die = Die()
    # Make some rolls, and store results in a list
    results = list()
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # Analyze the results
    frequencies = list()
    for value in range(1, die.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    print(frequencies)


if __name__ == '__main__':
    main()
