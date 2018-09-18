"""
Python 3.6
@Author: wrgsRay
"""
import csv
from matplotlib import pyplot as plt


def main():
    filename = 'sitka_weather_07-2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # for index, column_header in enumerate(header_row):
        #    print(index, column_header)
        highs = list()
        for row in reader:
            high = int(row[1])
            highs.append(high)


    # Plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    # Format plot
    plt.title('Daily high temperatures, July 2014')
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


if __name__ == '__main__':
    main()
