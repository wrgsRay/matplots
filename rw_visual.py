"""
Python 3.6
@Author: wrgsRay
"""
import matplotlib.pyplot as plt
from random_walk import RandomWalk


def main():
    # Keep making new waalks, as long as the program is active
    while True:
        rw = RandomWalk(50000)
        rw.fill_walk()

        plt.figure(figsize=(10, 6))
        point_numbers = list(range(rw.num_points))

        # plt.plot(rw.x_values, rw.y_values, linewidth=1)
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples, edgecolor='none', s=1)
        # Emphasize the first and last points.
        plt.scatter(0, 0, c='green', edgecolors='none', s=50)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

        # Remove the axes.
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()

        keep_running = input('Make another walk? (y/n):')
        if keep_running == 'n':
            break


if __name__ == '__main__':
    main()
