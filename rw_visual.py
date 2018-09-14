"""
Python 3.6
@Author: wrgsRay
"""
import matplotlib.pyplot as plt
from random_walk import RandomWalk


def main():
    # Keep making new waalks, as long as the program is active
    while True:
        rw = RandomWalk()
        rw.fill_walk()

        plt.scatter(rw.x_values, rw.y_values, s=1)
        plt.show()

        keep_running = input('Make another walk? (y/n):')
        if keep_running == 'n':
            break


if __name__ == '__main__':
    main()
