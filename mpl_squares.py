"""
Python 3.6
@Author: wrgsRay
"""
import matplotlib.pyplot as plt


def main():
    squares = [1, 4, 9, 16, 35]
    plt.plot(squares, linewidth=5)

    # Set chart title and label axes.
    plt.title('Square Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Square of Value', fontsize=14)

    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


if __name__ == '__main__':
    main()
