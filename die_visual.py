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
    for roll_num in range(100):
        result = die.roll()
        results.append(result)

    print(results)


if __name__ == '__main__':
    main()
