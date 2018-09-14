"""
Python 3.6
@Author: wrgsRay
"""
import matplotlib.pyplot as plt


def main():
    x_values = [x for x in range(1, 1001)]
    y_values = [x**2 for x in x_values]
    plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=10)

    # Set chart title and label axes.
    plt.title('Square Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Square of Value', fontsize=14)

    # Set size of tick labels.
    plt.tick_params(axis='both', which='major', labelsize=14)

    # Set the range for each axis.
    plt.axis([0, 1100, 0, 1100000])

    plt.show()


if __name__ == '__main__':
    main()
